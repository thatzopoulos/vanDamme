#!/bin/sh
echo 'RUNNING BEST PERFORMING DEEP Q LEARNING MODELS'
#python ../vanDamme.py --run_name basicRun --load_model True --model_savefile ../models/basicModels/basic-100-epochs-model.pth --scenario_config ../scenarios/basic.cfg --doom2_wad ../'Doom2.wad'
#python ../vanDamme.py --run_name rocketBasic --load_model True --model_savefile ../models/basicModels/rocketbasic-100-epochs-model.pth --scenario_config ../scenarios/rocket_basic.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --load_model True --model_savefile ../models/basicModels/myWayHome-100-epochs-model.pth --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --load_model True --model_savefile ../models/basicModels/myWayHome-100-epochs-model.pth --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --load_model True --model_savefile ../models/basicModels/myWayHome-100-epochs-model.pth --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
python ../vanDamme.py --run_name myWayHome --load_model True --model_savefile ../models/basicModels/myWayHome-100-epochs-model.pth --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'
#echo 'STEP LEARNING DEADLY CORRIDOR'
#python ../vanDamme.py --run_name deadlyCorridor --load_model True --model_savefile ../models/stepLearningModels/deadlyCorridor-100-epochs-model.pth --scenario_config ../scenarios/deadly_corridor.cfg --doom2_wad ../'Doom2.wad'

#echo 'RUNNING SHAPING VERSIONS'
#python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/health_gathering.cfg --doom2_wad ../'Doom2.wad'
#python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/take_cover.cfg --doom2_wad ../'Doom2.wad'
#python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/defend_the_line.cfg --doom2_wad ../'Doom2.wad'
#python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/health_gathering_supreme.cfg --doom2_wad ../'Doom2.wad'
#python ../vanDamme.py --set_to_shaping True --scenario_config ../scenarios/my_way_home.cfg --doom2_wad ../'Doom2.wad'

