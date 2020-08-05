# based on rastrigin from pymap_elites
# rewritten by Andrew James

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import map_elites.cvt as cvt_map_elites
import map_elites.common as cm_map_elites


# FUNCTION to compute

def vsr_simulate(params):
    amp_list = []
    freq_list = []
    phase_list = []
    p1_count = 0
    p2_count = 1
    p3_count = 2

    while (p1_count < len(params)):
        amp_list.append(params[p1_count] * 10)  # fits amp to [0,10]
        p1_count += 3
    while (p2_count < len(params)):
        freq_list.append(params[p2_count] * 4)  # fits freq to [0,10]
        p2_count += 3
    while (p3_count < len(params)):
        phase_list.append(params[p3_count] * 720)  # fits phase to [0, 720]
        p3_count += 3

    all_vox_string = ""
    for i in range(0, len(positions) - 1):
        coords = positions[i].split(",")
        all_vox_string += str(coords[0]) + ',' + str(coords[1]) + ',' + str(amp_list[i]) + ',' + str(
            freq_list[i]) + ',' + str(phase_list[i]) + '\n'
    last_vox = len(positions) - 1
    coords = positions[last_vox].split(",")
    all_vox_string += str(coords[0]) + ',' + str(coords[1]) + ',' + str(amp_list[last_vox]) + ',' + str(
        freq_list[last_vox]) + ',' + str(phase_list[last_vox])

    call_string = 'echo "' + all_vox_string + '" | java -cp 2dhmsr.jar it.units.erallab.hmsrobots.FineLocomotionStarter summary ' + terrain + ' ' + init_pos + ' ' + sim_time
    file = os.popen(call_string)
    output_string = file.read()
    metric_list = output_string.split(",\n")
    metric_dictionary = {}
    for metric in metric_list:
        entry = metric.split("=")
        metric_dictionary[entry[0]] = float(entry[1])

    fitness = metric_dictionary.get("ABS_INTEGRAL_Y")
    description = np.array([(metric_dictionary.get("DELTA_X")+100)/200, metric_dictionary.get("ABS_INTEGRAL_Y")/200])
    return fitness, description


if __name__ == "__main__":

    vox_file = open(sys.argv[1])
    global positions
    positions = vox_file.readlines()
    i = 0
    while i < len(positions):
        positions[i] = positions[i].replace("\n", "")
        i += 1

    global terrain
    terrain = str(sys.argv[2])
    global init_pos
    init_pos = str(sys.argv[3])
    global sim_time
    sim_time = str(sys.argv[4])

    # PARAMETERS - not sure what needs to be changed yet but I included them all w/ original explanations for clarity
    px = cm_map_elites.default_params.copy()

    # more of this -> higher-quality CVT
    px["cvt_samples"] = 100000

    # we evaluate in batches to parallelize
    px["batch_size"] = 20

    # proportion of niches to be filled before starting
    px["random_init"] = 0.7

    # batch for random initialization
    px["random_init_batch"] = 20

    # when to write results (one generation = one batch)
    px["dump_period"] = 20

    ####
    px["parallel"] = True

    # do we cache the result of CVT and reuse?
    px["cvt_use_cache"] = True

    # min/max of parameters
    px["min"] = 0
    px["max"] = 1

    # only useful if you use the 'iso_dd' variation operator
    px["iso_sigma"] = 0.01,
    px["line_sigma"] = 0.2

    archive = cvt_map_elites.compute(2, len(positions)*3, vsr_simulate, n_niches=50, max_evals=500, log_file=open('cvt.dat', 'w'), params=px)
