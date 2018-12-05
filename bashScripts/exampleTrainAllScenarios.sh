#!/bin/sh

python ../vanDamme.py --run_name basicRun --save_model True --model_savefile ../models/exampleFolder/basic-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name defendTheCenter --save_model True --model_savefile ../models/exampleFolder/defendTheCenter-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/defend_the_center.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name healthGathering --save_model True --model_savefile ../models/exampleFolder/healthGathering-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/health_gathering.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name deadlyCorridor --save_model True --model_savefile ../models/exampleFolder/deadlyCorridor-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/deadly_corridor.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --save_model True --model_savefile ../models/exampleFolder/myWayHome-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name defendTheLine --save_model True --model_savefile ../models/exampleFolder/defendTheLine-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/defend_the_line.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name predictPosition --save_model True --model_savefile ../models/exampleFolder/predictPosition-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/predict_position.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name rocketBasic --save_model True --model_savefile ../models/exampleFolder/rocketbasic-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/rocket_basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name takeCover --save_model True --model_savefile ../models/exampleFolder/takeCover-100-epochs-model.pth --epochs 100 --scenario_config ../scenarios/take_cover.cfg --doom2_wad ../'Doom2.wad'
