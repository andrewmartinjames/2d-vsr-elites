# 2dsoro
Connecting Python3 Map-Elites to 2d-VSR-Sim.

#### Dependencies:
* python3
* numpy
* scikit-learn
* matplotlib

## `experiment.py`:
experiment.py takes four arguments:
1. a text file containing the position data for each voxel included in the robot
  * each voxel is described as x_pos,y_pos where x_pos and y_pos are integers starting at 0 that describe the position of the voxel within the full robot
  * each voxel is on a separate line
2. a string formatted to describe the shape of the terrain the robot will traverse
3. the starting x position of the robot in that terrain
4. the time to run each simulation

#### Usage:
To run an example experiment:

`python experiment.py example.txt 1,0:1000,100:2000,10 1000 30`

(may require `python3` instead of `python` depending on system default)

* `example.txt` contains an example robot description
* `1,0:1000,100:2000,10` produces a 2000-unit terrain with a small, 100-unit hill with a peak at the map's halfway point
* `1000` is the starting x-position of the robot, in this case on top of the hill
* `30` is the length in seconds of each run of the simulation


#### Current in-use voxel parameter ranges:
Each voxel is independently controlled sinusoidally within the following ranges:
1. Amplitude: [0,10] - no unit
2. Frequency: [0,10] - in Hz
3. Phase: [0,720] - in 1/2 degree


#### Archive format:
Archive files are formatted with information about one elite per line, as follows:

`fitness centroid_x_val centroid_y_val description_x_val description_theta_val param_0, param_1 ...`

where all remaining values in the line are parameter inputs to the simulation function.

## `make_videos.py`:
#### Usage:
`make_videos.py` takes 5 arguments, and requires that an archive file already be generated. The same arguments used for `experiment.py` should be used in `make_videos.py` to produce useful results. Videos take a while to save, and are named after the fitness value in the archive of the elite they correspond to. The call for `make_videos` is:

`python make_videos.py example.txt 1,0:1000,100:2000,10 1000 30 archive_500.dat`

using all the same arguments as `experiment.py` with the addition of the archive file whose elites should be turned into videos. If only some of the elites need to be viewed, an abbreviated version of the archive can be saved with only the lines containing the desired elites.

## Citations
1. Medvet, Bartoli, De Lorenzo, Seriani. "[Design, Validation, and Case Studies of 2D-VSR-Sim, an Optimization-friendly Simulator of 2-D Voxel-based Soft Robots](https://arxiv.org/abs/2001.08617)" arXiv cs.RO: 2001.08617
2. Mouret JB, Clune J. Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909. 2015 Apr 20.
3. Vassiliades V, Chatzilygeroudis K, Mouret JB. Using centroidal voronoi tessellations to scale up the multi-dimensional archive of phenotypic elites algorithm. IEEE Transactions on Evolutionary Computation. 2017 Aug 3.
4. Vassiliades V, Mouret JB. Discovering the Elite Hypervolume by Leveraging Interspecies Correlation. Proc. of GECCO. 2018.
5. Mouret JB, Maguire G. Quality Diversity for Multi-task Optimization. Proc of GECCO. 2020.
