# based on rastrigin from pymap_elites
# rewritten by Andrew James

import sys, os, subprocess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import math
import map_elites.cvt as cvt_map_elites
import map_elites.common as cm_map_elites



# FUNCTION to compute

def vsr_simulate(params):
    #### PARAMS FOR SYSTEM INPUT, NEED TO CHANGE SO THAT vsr_simulate(params) -> needed inputs
    x_pos = 0
    y_pos = 0
    amp = 1
    freq = 1
    phase = 0

    #### SYSTEM CALL CONSTRUCTION, NEED TO CHANGE TO DESIRED METHOD OF INPUTTING VOXELS
    call_string = 'echo "' + str(x_pos) + ',' + str(y_pos) + ',' + str(amp) + ',' + str(freq) + ',' + str(phase) + '\n' \
                  + '1,1,5,2,1"' + ' | java -cp 2dhmsr.jar it.units.erallab.hmsrobots.FineLocomotionStarter summary 1,0:1000,100:2000,10 1000 30'

    #### SYSTEM CALL, this part is basically done
    file = os.popen(call_string)
    string_of_file = file.read()


    #### CONVERT SYSTEM OUTPUT TO fitness + description - NO WORK DONE YET ON THIS
    fitness = 1
    description = [1,1]
    return fitness, description



# PARAMETERS - not sure what needs to be changed yet but I included them all w/ original explanations for clarity
px = cm_map_elites.default_params.copy()

# more of this -> higher-quality CVT
px["cvt_samples"] = 25000

# we evaluate in batches to parallelize
px["batch_size"] = 200

# proportion of niches to be filled before starting
px["random_init"] = 0.1

# batch for random initialization
px["random_init_batch"] = 100

# when to write results (one generation = one batch)
px["dump_period"] = 100000

#### no parallelization for now, it might break shit
px["parallel"] = False

# do we cache the result of CVT and reuse?
px["cvt_use_cache"] = True

# min/max of parameters
px["min"] = 0
px["max"] = 1

# only useful if you use the 'iso_dd' variation operator
px["iso_sigma"] = 0.01,
px["line_sigma"] = 0.2


archive = cvt_map_elites.compute(2, 10, vsr_simulate, n_niches=10000, max_evals=1e6, log_file=open('cvt.dat', 'w'), params=px)
