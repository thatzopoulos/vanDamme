from __future__ import division
from __future__ import print_function
from vizdoom import *
import itertools as it
from random import sample, randint, random, choice
from time import time, sleep
import numpy as np
import skimage.color, skimage.transform
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
from tqdm import trange
import argparse
import os

#NON PARSED VARIABLES
discount_factor = 0.99
replay_memory_size = 10000

# NN learning settings
batch_size = 64

# Training regime
test_episodes_per_epoch = 100

# Other parameters
frame_repeat = 12
resolution = (30, 45)
episodes_to_watch = 10

model_folder = 'models/'

scenario_folder = 'scenarios/'
# config_file_path = "../../scenarios/basic.cfg"


####PARSER
parser = argparse.ArgumentParser(description='VanDamme Parameter Parser')

parser.add_argument("--run_name", type=str, action='store',default="default",
                    help="Run name")
parser.add_argument("--learning_rate", type=int, default=.00025,
                        help="Learning Rate")
parser.add_argument("--epochs", type=int, default=20,
                        help="Number of test episodes per epoch")
parser.add_argument("--learning_steps_per_epoch", type=int, default=2000,
                        help="Learning Steps Per Epoch")
parser.add_argument("--replay_memory_size", type=int, default=10000,
                        help="replay_memory_size")
parser.add_argument("--model_savefile", type=str, action='store',default="unnammedModel.pth",
	help="Saved Model Name")
parser.add_argument("--save_model", type=bool, action='store', default=False, help="Save Model")
parser.add_argument("--load_model", type=bool, action='store', default=False, help="Save Model")
parser.add_argument("--scenario_config", type=str, action='store',default="basic.cfg",
	help="Scenario Choice")
parser.add_argument("--set_to_shaping", type=bool, action='store',default=False,
    help="Use Shaping to improve run time instead of DQN, does not save a model")
parser.add_argument("--doom2_wad", type=str, action='store',default="Doom2.wad",
    help="Location of Doom2 wad file, defaults to current folder")


args = parser.parse_args()
if args.save_model is True:
	save_model = True
	load_model = False
	skip_learning = False
	print("Save Mode")
	print(args.model_savefile)
if args.load_model is True:
	save_model = False
	load_model = True
	skip_learning = True
	print("Load Mode")
if args.set_to_shaping is True:
    print("Running Shaping")
if args.set_to_shaping is False:
    print("Running Deep Q Learning")





# Q-learning settings
learning_rate = args.learning_rate
epochs = args.epochs

learning_steps_per_epoch = args.learning_steps_per_epoch


# STEP LEARNING
#learning_step = .1
#if epochs % 5:
#    learning_rate = learning_step*learning_rate


model_savefile = args.model_savefile
config_file_path = args.scenario_config

print(args.run_name)


####FUNCTIONS
# Converts and down-samples the input image
def preprocess(img):
    img = skimage.transform.resize(img, resolution)
    img = img.astype(np.float32)
    return img


class ReplayMemory:
    def __init__(self, capacity):
        channels = 1
        state_shape = (capacity, channels, resolution[0], resolution[1])
        self.s1 = np.zeros(state_shape, dtype=np.float32)
        self.s2 = np.zeros(state_shape, dtype=np.float32)
        self.a = np.zeros(capacity, dtype=np.int32)
        self.r = np.zeros(capacity, dtype=np.float32)
        self.isterminal = np.zeros(capacity, dtype=np.float32)

        self.capacity = capacity
        self.size = 0
        self.pos = 0

    def add_transition(self, s1, action, s2, isterminal, reward):
        self.s1[self.pos, 0, :, :] = s1
        self.a[self.pos] = action
        if not isterminal:
            self.s2[self.pos, 0, :, :] = s2
        self.isterminal[self.pos] = isterminal
        self.r[self.pos] = reward

        self.pos = (self.pos + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def get_sample(self, sample_size):
        i = sample(range(0, self.size), sample_size)
        return self.s1[i], self.a[i], self.s2[i], self.isterminal[i], self.r[i]


class Net(nn.Module):
    def __init__(self, available_actions_count):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=6, stride=3)
        self.conv2 = nn.Conv2d(8, 8, kernel_size=3, stride=2)
        self.fc1 = nn.Linear(192, 128)
        self.fc2 = nn.Linear(128, available_actions_count)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 192)
        x = F.relu(self.fc1(x))
        return self.fc2(x)

criterion = nn.MSELoss()


def learn(s1, target_q):
    s1 = torch.from_numpy(s1)
    target_q = torch.from_numpy(target_q)
    s1, target_q = Variable(s1), Variable(target_q)
    output = model(s1)
    loss = criterion(output, target_q)
    # compute gradient and do SGD step
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss

def get_q_values(state):
    state = torch.from_numpy(state)
    state = Variable(state)
    return model(state)

def get_best_action(state):
    q = get_q_values(state)
    m, index = torch.max(q, 1)
    action = index.data.numpy()[0]
    return action


def learn_from_memory():
    """ Learns from a single transition (making use of replay memory).
    s2 is ignored if s2_isterminal """

    # Get a random minibatch from the replay memory and learns from it.
    if memory.size > batch_size:
        s1, a, s2, isterminal, r = memory.get_sample(batch_size)

        q = get_q_values(s2).data.numpy()
        q2 = np.max(q, axis=1)
        target_q = get_q_values(s1).data.numpy()
        # target differs from q only for the selected action. The following means:
        # target_Q(s,a) = r + gamma * max Q(s2,_) if isterminal else r
        target_q[np.arange(target_q.shape[0]), a] = r + discount_factor * (1 - isterminal) * q2
        learn(s1, target_q)


def perform_learning_step(epoch):
    """ Makes an action according to eps-greedy policy, observes the result
    (next state, reward) and learns from the transition"""

    def exploration_rate(epoch):
        """# Define exploration rate change over time"""
        start_eps = 1.0
        end_eps = 0.1
        const_eps_epochs = 0.1 * epochs  # 10% of learning time
        eps_decay_epochs = 0.6 * epochs  # 60% of learning time

        if epoch < const_eps_epochs:
            return start_eps
        elif epoch < eps_decay_epochs:
            # Linear decay
            return start_eps - (epoch - const_eps_epochs) / \
                               (eps_decay_epochs - const_eps_epochs) * (start_eps - end_eps)
        else:
            return end_eps

    s1 = preprocess(game.get_state().screen_buffer)

    # With probability eps make a random action.
    eps = exploration_rate(epoch)
    if random() <= eps:
        a = randint(0, len(actions) - 1)
    else:
        # Choose the best action according to the network.
        s1 = s1.reshape([1, 1, resolution[0], resolution[1]])
        a = get_best_action(s1)
    reward = game.make_action(actions[a], frame_repeat)

    isterminal = game.is_episode_finished()
    s2 = preprocess(game.get_state().screen_buffer) if not isterminal else None

    # Remember the transition that was just experienced.
    memory.add_transition(s1, a, s2, isterminal, reward)

    learn_from_memory()


# Creates and initializes ViZDoom environment.
def initialize_vizdoom(config_file_path):
    print("Initializing doom...")
    game = DoomGame()
    game.load_config(config_file_path)
    game.set_window_visible(False)
    game.set_mode(Mode.PLAYER)
    game.set_screen_format(ScreenFormat.GRAY8)
    game.set_screen_resolution(ScreenResolution.RES_640X480)
    #game.set_doom_game_path("Doom2.wad")
    #game.init()
    print("Doom initialized.")
    return game


if __name__ == '__main__':

#TODO FOR SHAPING VERSION CALL
    if args.set_to_shaping == False:
        # Create Doom instance
        game = initialize_vizdoom(config_file_path)
        game.set_doom_game_path(args.doom2_wad)
        game.init()

        # Action = which buttons are pressed
        n = game.get_available_buttons_size()
        actions = [list(a) for a in it.product([0, 1], repeat=n)]

        # Create replay memory which will store the transitions
        memory = ReplayMemory(capacity=replay_memory_size)

        if load_model:
            print("Loading model from: ", model_savefile)
            model = torch.load(model_savefile)
        else:
            model = Net(len(actions))
        
        optimizer = torch.optim.SGD(model.parameters(), learning_rate)

        print("Starting the training!")
        time_start = time()
        if not skip_learning:
            for epoch in range(epochs):
                print("\nEpoch %d\n-------" % (epoch + 1))
                train_episodes_finished = 0
                train_scores = []

                print("Training...")
                game.new_episode()
                for learning_step in trange(learning_steps_per_epoch, leave=False):
                    perform_learning_step(epoch)
                    if game.is_episode_finished():
                        score = game.get_total_reward()
                        train_scores.append(score)
                        game.new_episode()
                        train_episodes_finished += 1

                print("%d training episodes played." % train_episodes_finished)

                train_scores = np.array(train_scores)

                print("Results: mean: %.1f +/- %.1f," % (train_scores.mean(), train_scores.std()), \
                      "min: %.1f," % train_scores.min(), "max: %.1f," % train_scores.max())

                print("\nTesting...")
                test_episode = []
                test_scores = []
                for test_episode in trange(test_episodes_per_epoch, leave=False):
                    game.new_episode()
                    while not game.is_episode_finished():
                        state = preprocess(game.get_state().screen_buffer)
                        state = state.reshape([1, 1, resolution[0], resolution[1]])
                        best_action_index = get_best_action(state)

                        game.make_action(actions[best_action_index], frame_repeat)
                    r = game.get_total_reward()
                    test_scores.append(r)

                test_scores = np.array(test_scores)
                print("Results: mean: %.1f +/- %.1f," % (
                    test_scores.mean(), test_scores.std()), "min: %.1f" % test_scores.min(),
                      "max: %.1f" % test_scores.max())

                print("Saving the network weights to:", model_savefile)
                torch.save(model, model_savefile)

                print("Total elapsed time: %.2f minutes" % ((time() - time_start) / 60.0))

        game.close()
        print("======================================")
        print("Training finished. Beginning the Kumite")

        # Reinitialize the game with window visible
        game.set_window_visible(True)
        game.set_mode(Mode.ASYNC_PLAYER)
        game.init()
        
        averageScore = 0
        for _ in range(episodes_to_watch):
            game.new_episode()
            while not game.is_episode_finished():
                state = preprocess(game.get_state().screen_buffer)
                state = state.reshape([1, 1, resolution[0], resolution[1]])
                best_action_index = get_best_action(state)

                # Instead of make_action(a, frame_repeat) in order to make the animation smooth
                game.set_action(actions[best_action_index])
                for _ in range(frame_repeat):
                    game.advance_action()

            # Sleep between episodes
            sleep(1.0)
            score = game.get_total_reward()
            print("Total score: ", score)
            averageScore = averageScore+score
        print("Average Score: ", (averageScore/episodes_to_watch))

    if args.set_to_shaping == True:
        print("Shaping")
        game = DoomGame()
        game.load_config(config_file_path)
        game.set_window_visible(True)
        game.set_screen_format(ScreenFormat.GRAY8)
        game.set_screen_resolution(ScreenResolution.RES_640X480)
        game.set_doom_game_path(args.doom2_wad)
        game.init()
        print("Doom initialized.")
       # Creates all possible actions.
        actions_num = game.get_available_buttons_size()
        actions = []
        for perm in it.product([False, True], repeat=actions_num):
            actions.append(list(perm))

        episodes = 10
        sleep_time = 0.028

        for i in range(episodes):

            print("Episode:" + str(i + 1))
            game.new_episode()
            last_total_shaping_reward = 0

            while not game.is_episode_finished():
                state = game.get_state()
                reward = game.make_action(choice(actions))
                fixed_shaping_reward = game.get_game_variable(vizdoom.GameVariable.USER1)  # Get value of scripted variable
                shaping_reward = vizdoom.doom_fixed_to_double(
                    fixed_shaping_reward)  # If value is in DoomFixed format project it to double
                shaping_reward = shaping_reward - last_total_shaping_reward
                last_total_shaping_reward += shaping_reward

                print("State #" + str(state.number))
                print("Health: ", state.game_variables[0])
                print("Last Reward:", reward)
                print("Last Shaping Reward:", shaping_reward)
                print("=====================")
                if sleep_time > 0:
                    sleep(sleep_time)
            print("Episode finished!")
            print("Total reward:", game.get_total_reward())
            print('========================')


#print(args.run_name)


#print('========== Running DOOM ==========')

# load DOOM
#parse_game_args(remaining)
