#!/bin/sh
echo 'RUNNING ORIGINAL MODELS'
python ../vanDamme.py --run_name basicRun --load_model True --model_savefile ../models/basicModels/basic-100-epochs-model.pth --scenario_config ../scenarios/basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name defendTheCenter --load_model True --model_savefile ../models/basicModels/defendTheCenter-100-epochs-model.pth --scenario_config ../scenarios/defend_the_center.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name healthGathering --load_model True --model_savefile ../models/basicModels/healthGathering-100-epochs-model.pth --scenario_config ../scenarios/health_gathering.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name deadlyCorridor --load_model True --model_savefile ../models/basicModels/deadlyCorridor-100-epochs-model.pth --scenario_config ../scenarios/deadly_corridor.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --load_model True --model_savefile ../models/basicModels/myWayHome-100-epochs-model.pth --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name defendTheLine --load_model True --model_savefile ../models/basicModels/defendTheLine-100-epochs-model.pth --scenario_config ../scenarios/defend_the_line.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name predictPosition --load_model True --model_savefile ../models/basicModels/predictPosition-100-epochs-model.pth --scenario_config ../scenarios/predict_position.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name rocketBasic --load_model True --model_savefile ../models/basicModels/rocketbasic-100-epochs-model.pth --scenario_config ../scenarios/rocket_basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name takeCover --load_model True --model_savefile ../models/basicModels/takeCover-100-epochs-model.pth --scenario_config ../scenarios/take_cover.cfg --doom2_wad ../'Doom2.wad'

echo 'RUNNING STEP LEARNING MODELS'
python ../vanDamme.py --run_name basicRun --load_model True --model_savefile ../models/stepLearningModels/basic-100-epochs-model.pth --scenario_config ../scenarios/basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name defendTheCenter --load_model True --model_savefile ../models/stepLearningModels/defendTheCenter-100-epochs-model.pth --scenario_config ../scenarios/defend_the_center.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name healthGathering --load_model True --model_savefile ../models/stepLearningModels/healthGathering-100-epochs-model.pth --scenario_config ../scenarios/health_gathering.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name deadlyCorridor --load_model True --model_savefile ../models/stepLearningModels/deadlyCorridor-100-epochs-model.pth --scenario_config ../scenarios/deadly_corridor.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --load_model True --model_savefile ../models/stepLearningModels/myWayHome-100-epochs-model.pth --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name defendTheLine --load_model True --model_savefile ../models/stepLearningModels/defendTheLine-100-epochs-model.pth --scenario_config ../scenarios/defend_the_line.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name predictPosition --load_model True --model_savefile ../models/stepLearningModels/predictPosition-100-epochs-model.pth --scenario_config ../scenarios/predict_position.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name rocketBasic --load_model True --model_savefile ../models/stepLearningModels/rocketbasic-100-epochs-model.pth --scenario_config ../scenarios/rocket_basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name takeCover --load_model True --model_savefile ../models/stepLearningModels/takeCover-100-epochs-model.pth --scenario_config ../scenarios/take_cover.cfg --doom2_wad ../'Doom2.wad'

echo 'Running Increased Learning Steps Models'
python ../vanDamme.py --run_name defendTheCenter --load_model True --model_savefile ../models/replay20000/defendTheCenterReplay2000.pth --scenario_config ../scenarios/defend_the_center.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name healthGathering --load_model True --model_savefile ../models/replay20000/healthGatheringReplay2000.pth --scenario_config ../scenarios/health_gathering.cfg --doom2_wad ../'Doom2.wad'

echo 'Running Shaping Version of HealthGathering and Take Cover'
python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/health_gathering.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/take_cover.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/defend_the_line.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/health_gathering_supreme.cfg --doom2_wad ../'Doom2.wad'
