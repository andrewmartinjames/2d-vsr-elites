# based on rastrigin from pymap_elites
# rewritten by Andrew James

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import math
import map_elites.cvt as cvt_map_elites
import map_elites.common as cm_map_elites



# FUNCTION to compute

def vsr_simulate(params):
    metric = None   # fill in with code that calls 2dhmsr with given params
    return metric



# PARAMETERS - not sure what needs to be changed yet but I included them all w/ original explanations for clarity

px = cm_map_elites.default_params.copy()

# more of this -> higher-quality CVT
px["cvt_samples"] = 25000

# we evaluate in batches to paralleliez
px["batch_size"] = 200

# proportion of niches to be filled before starting
px["random_init"] = 0.1

# batch for random initialization
px["random_init_batch"] = 100

# when to write results (one generation = one batch)
px["dump_period"] = 100000

# do we use several cores?
px["parallel"] = True

# do we cache the result of CVT and reuse?
px["cvt_use_cache"] = True

# min/max of parameters
px["min"] = 0
px["max"] = 1

# only useful if you use the 'iso_dd' variation operator
px["iso_sigma"] = 0.01,
px["line_sigma"] = 0.2


archive = cvt_map_elites.compute(2, 10, rastrigin, n_niches=10000, max_evals=1e6, log_file=open('cvt.dat', 'w'), params=px)
