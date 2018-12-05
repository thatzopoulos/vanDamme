# VanDamme

Arnold is a PyTorch implementation of a VizDoom bot trained using Deep Q Reinforcement Learning.


### This repository contains:
- The source code to train DOOM agents
- Scenarios for the bot to perform on
- Pretrained Models
- Bash Scripts to load and train batches of models at once

## Installation

#### Dependencies
VanDamme was written and tested on a Linux machine using the Anaconda environment found in: pytorch.yaml

## Code structure

    .
    ├── bashScripts     # Bash Scripts to Load and Save Multiple Models
    ├── Models          # Pretrained Models
    ├── previousRuns    #Text files of output of previous runs
    ├── Scenarios       #Scenarios and wad files to load
    ├── vanDamme.py     # Main File
    ├── pytorch.yaml    # Anaconda yaml file
    └── README.md

## Train a model

The parameters that can be specified during a run of VanDamme can be seen below:


```bash
python vanDamme.py

## General parameters about the game
--run_name "ExampleName"        
--learning_rate ".00025"     
--epochs "20"                   
--learning_steps_per_epoch "2000" 
--replay_memory_size "10000"   
--model_savefile "unnamedModel.pth"
--save_model "False"
--load_model "False"
--scenario_config "basic.cfg"
--set_to_shaping "False"
--doom2_wad "Doom2.wad"
```

## Acknowledgements
The map and scenario files have been borrowed from the ViZDoom repository. Doom2.wad was obtained from a purchased copy of Doom 2.