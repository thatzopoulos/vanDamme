# VanDamme

VanDamme is a PyTorch implementation of a VizDoom bot trained using Deep Q Reinforcement Learning.


### This repository contains:
- The source code to train DOOM agents
- Scenarios for the bot to perform on
- Pretrained Models
- Bash Scripts to load and train batches of models at once

## Installation

#### Dependencies
VanDamme was written and tested on a Linux machine and all dependencies can be installed using the Anaconda environment yaml file: pytorch.yaml

## Code structure

    .
    ├── bashScripts     # Bash Scripts to Load and Save Multiple Models
    ├── models          # Pretrained Models
    ├── previousRuns    # Text files of full output of previous runs
    ├── researchpapers  # Example Research Papers on vizdoom training and DQN
    ├── scenarios       # Scenarios and wad files to load
    ├── vanDamme.py     # Main File
    ├── pytorch.yaml    # Anaconda yaml file
    ├── Doom2.wad    	# Assets from original Doom 2, all models were trained using this   
    └── README.md

## Using the VanDamme Parser

The parameters that can be specified during a run of VanDamme are shown below:


```bash
python vanDamme.py

## Arguments used by the vanDamme parser and their default settings
--run_name "ExampleName"        
--learning_rate .00025     
--epochs 20                   
--learning_steps_per_epoch 2000 
--replay_memory_size 10000  
--model_savefile "unnamedModel.pth"
--save_model False
--load_model False
--scenario_config "basic.cfg"
--set_to_shaping "False"
--doom2_wad "Doom2.wad"
```
