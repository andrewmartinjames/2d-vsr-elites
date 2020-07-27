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
    amp_list = []
    freq_list = []
    phase_list =[]
    p1_count = 0
    p2_count = 1
    p3_count = 2
    while (p1_count < len(params)):
        amp_list.append(params[p1_count]*10)
        p1_count += 3
    while (p2_count < len(params)):
        freq_list.append(params[p2_count] MODIFIED TO FIT FREQ RANGE)
        p2_count += 3
    while (p3_count < len(params)):
        phase_list.append(params[p3_count] MODIFIED TO FIT -720,720)

    all_vox_string = ""
    for i in range(0,len(positions)-1):
        coords = positions[i].split(",")
        all_vox_string += str(coords[0]) + ',' + str(coords[1]) + ',' + str(amp_list[i]) + ',' + str(freq_list[i]) + ',' + str(phase_list[i]) + '\n'
    last_vox = len(positions) - 1
    coords = positions[last_vox].split(",")
    all_vox_string += str(coords[0]) + ',' + str(coords[1]) + ',' + str(amp_list[last_vox]) + ',' + str(freq_list[last_vox]) + ',' + str(phase_list[last_vox])


    #### SYSTEM CALL CONSTRUCTION, NEED TO CHANGE TO DESIRED METHOD OF INPUTTING VOXELS
    call_string = 'echo "' + all_vox_string + ' | java -cp 2dhmsr.jar it.units.erallab.hmsrobots.FineLocomotionStarter summary ' + terrain + ' ' + init_pos + ' ' + sim_time

    #### SYSTEM CALL, this part is basically done
    file = os.popen(call_string)
    output_string = file.read()


    #### CONVERT SYSTEM OUTPUT TO fitness + description - NO WORK DONE YET ON THIS
    fit = 1
    desc = [1,1]
    return fit, desc


if __name__ == "__main__":

    vox_file = open(sys.argv[1])
    global positions
    positions = vox_file.readlines()
    for pos in positions:
        pos.strip("\n")

    global terrain
    terrain = sys.argv[2]
    global init_pos
    init_pos = sys.argv[3]
    global sim_time
    sim_time = sys.argv[4]

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


    archive = cvt_map_elites.compute(2, len(positions)*3, vsr_simulate, n_niches=10000, max_evals=1e6, log_file=open('cvt.dat', 'w'), params=px)
