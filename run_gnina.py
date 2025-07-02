import os
from code import run_gnina_docking

PATH_TO_ST = "example/1a42_processed.pdb"
PATH_TO_LIG = "example/YMZ_ideal.sdf"
PATH_TO_OUTPUT = "example/docked_YMZ.sdf"

config = {
    "center_x": -6,
    "center_y": 0,
    "center_z": 15,
    "exhaustiveness": 8,
    "cnn_scoring": 'none',
    "cpu": 8,
    "num_modes": 1
}

run_gnina_docking(PATH_TO_ST, PATH_TO_LIG, PATH_TO_OUTPUT, config)