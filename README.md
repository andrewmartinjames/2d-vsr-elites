# 2d-vsr-elites
A package connecting Python3 Map-Elites to 2d-VSR-Sim for fast prototyping of simple 2d voxel robots. 

This was a summer research project by Andrew James and [Ali Ahmed Khan](https://github.com/Ahmed4812) for Prof. John Rieffel's lab at Union College. It's based on Eric Medvet's [2d-vsr-sim](https://github.com/ericmedvet/2dhmsr) and Jean-Baptiste Mouret (& the Resibots team)'s [pymap_elites](https://github.com/resibots/pymap_elites). Further relevant citations are at the bottom of the readme.

## **Introduction**

#### Dependencies:
* python3
* numpy
* scikit-learn
* matplotlib

#### Structure:
2dsoro is organized into folders based on the two packages it connects (tree only shows files relevant to running and creating new experiments):
```
├── 2d-vsr-sim
│   └── src/main/java/it/units/erallab/hmsrobots
│       ├── FineLocomotionStarter.java              
│       └── tasks
│           └── Locomotion.java                       
└── pymap_elites
    ├── 2dhmsr.jar
    ├── afprobot
    │   ├── afp_robot.py
    │   └── make_videos.py
    ├── phasesrobot
    │   ├── make_videos_phases.py
    │   └── phases_robot.py
    ├── plot
    │   └── plot_2d_map.py
    └── robotdescriptions
        ├── example.txt
        ├── horizontal.txt
        ├── longBody_smallLegs.txt
        ├── rect.txt
        ├── spikeball.txt
        └── vertical.txt
```
The Java package `2d-vsr-sim` is compiled into `2dhmsr.jar` in pymap_elites with `FineLocomotionStarter` configured as the launch class. This class controls individual simulations of robots by the package, with several possible interfaces, including output of performance metrics, individual voxel positions, GUI windows, and saved video files.

2dsoro's implementation of `pymap_elites` uses two modules for each type of desired evolutionary experiment: a module that runs the evolutionary algorithm and saves the resulting behaviors to an archive, and a module that takes that archive file and the corresponding input parameters and creates videos of the simulation runs.

`afprobot` and `phasesrobot` are currently the two types of experiments available, each described below. `afp_robot` and `phases_robot` are their respective evolutionary modules, while `make_videos` and `make_videos_phases` are their video modules.

`plot` contains several modules that can be run after an evolutionary experiment is complete to visually represent what behaviors were found. `plot_2d_map` is of most use to us, and is described in detail below.

`robotdescriptions` contains text files with voxel positions on individual lines that correspond to the shape of a desired 2d voxel-based robot. Each voxel is written as `x,y`, where x and y correspond to its position on an arbitrarily sized grid starting at 0,0. These robot description files are best understood by opening one in a text editor and viewing the contents.

## **afprobot** - amplitude, frequency, phase

The `afprobot` type assigns different amplitude, frequency, and phase parameters for each voxel in each tested robot during evolution. This leads to a high parameter-space, since each voxel has 3 parameters to evolve on. The results from this experiment type are frequently less successful in terms of distance traveled due to the degree of complication. However, it is a good starting point to understand how all of the parameters can be controlled.

### Usage

***The modules used to run experiments for `2dsoro` expect to be called from a command line pointed at the pymap_elites folder. If the listed directory is different, first navigate to the pymap_elites folder before making any Python calls.***

##### Evolution
The first step in using `afprobot` is to run the evolutionary algorithm on the desired robot and terrain. The CLI call for this is:

`python3 afprobot/afp_robot.py robots/[your_robot.txt] [terrain_descriptor] [starting_position] [simulation_time]`

* `your_robot.txt` should be replaced with the text file describing the desired robot
* `terrain_descriptor` is formatted to describe the terrain for a robot to walk on
  * the string should be formatted in `x,y` pairs separated by colons `:` that describe elevation points to form a terrain with
  * e.g. `1,0:1000,200:2000,100` describes a terrain with a hill with a steep increase and a more gradual decrease
* `starting position` describes the starting x-position of the leftmost voxel on the robot; the starting y-position is determined by the terrain height at this point so that the robot starts right above the ground
* `simulation_time` is the length of each simulation run in seconds of virtual time
* for an example, run `python3 afprobot/afp_robot.py robots/example.txt 1,0:1000,200:2000,100 1000 30`

When the evolutionary algorithm is finished, a number of `archive_xxx.dat` files will have been saved to the main folder, along with single `centroids_...` and `cvt.dat` files. These archives contain the parameters and results of "elite" simulation runs, and are ready to be tuned into videos.

##### Videos
Once the `archive` files are saved and `afp_robot.py` has terminated, video files of the elite behaviors found can be generated  using `make_videos.py` with the following CLI call:

`python3 afprobot/make_videos.py robots/[your_robot.txt] [terrain_descriptor] [starting_position] [simulation_time] [archive_file]`
* All `[parameters]` used (except `[archive_file]`) should be the same as what was used for the evolution call; if there are differences, the videos produced will not be accurate
* `[archive_file]` can point to any one of the archives generated by the evolution, but generally the latest (highest-numbered) will have the most useful behaviors.
  * If the videos are taking too long to process, or if some of the elites found are not of interest, a modified version of the archive file with only the interesting elites can be saved and used instead.

Videos are saved in `.mov` format to the `pymap_elites` folder (for now).

## **phasesrobot**
The `phasesrobot` experiment type assigns only one frequency and amplitude to all of the voxels in a simulation run, but can assign different phases either to each voxel or to each column of voxels in a robot. These robots typically travel much further and present more stable behaviors due to their synced frequency. Note that frequency and amplitude are not held constant across multiple simulation runs; they can still be varied, but there is only one frequency and one amplitude parameter for the entire robot, reducing paramter-space significantly.

### Usage

***The modules used to run experiments for `2dsoro` expect to be called from a command line pointed at the pymap_elites folder. If the listed directory is different, first navigate to the pymap_elites folder before making any Python calls.***

##### Evolution
Running the evolutionary algorithm is largely similar to `afprobot` but with an extra argument:

`python3 phasesrobot/phases_robot.py robots/[your_robot.txt] [terrain_descriptor] [starting_position] [simulation_time] [variance_type]`
* `variance_type` describes whether each voxel in a robot should have its own phase, or whether voxels in the same column (same y-value in description) should have the same phase. The two options are:
  * `by_voxel` - 1 phase/voxel
  * `by_column` - 1 phase/column of voxels
* All other arguments function in the same way as they do for `afp_robot`, described above.

##### Videos:
Creating videos of the results works similarly to `afprobot` as well, requiring the same input arguments as were used in the evolutionary algorithm call as well as the desired archive file:

`python3 phasesrobot/make_videos_phases.py robots/[your_robot.txt] [terrain_descriptor] [starting_position] [simulation_time] [variance_type] [archive_file]`
* This works identically to the videos call in `afprobot`, but adds the `[variance_type]` as an input argument before the archive file.

## **plot**
Plot offers several methods of visualizing evolutionary results, but the most useful is `plot_2d_map`.

### plot_2d_map
`plot_2d_map.py` produces .png and .pdf outputs of a map displaying the elite behaviors found by evolution.
##### Usage
***The modules used to run experiments for `2dsoro` expect to be called from a command line pointed at the pymap_elites folder. If the listed directory is different, first navigate to the pymap_elites folder before making any Python calls.***

`plot_2d_map` is called quite simply:

`python3 plot/plot_2d_map.py [centroids_file] [archive_file]`
* `[centroids_file]` is produced by running an evolution, and should be found in the main pymap_elites folder named something like "centroids_50_2.dat"
* `[archive_file]` is the same as would be used to make videos; located in pymap_elites, with the highest numbered (e.g. "archive_500.dat") being the most recent.

Producing plots this way allows the researcher to see which specific niches were filled in the course of a given evolutioanry experiment.



## **Citations**
1. Medvet, Bartoli, De Lorenzo, Seriani. "[Design, Validation, and Case Studies of 2D-VSR-Sim, an Optimization-friendly Simulator of 2-D Voxel-based Soft Robots](https://arxiv.org/abs/2001.08617)" arXiv cs.RO: 2001.08617
2. Mouret JB, Clune J. Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909. 2015 Apr 20.
3. Vassiliades V, Chatzilygeroudis K, Mouret JB. Using centroidal voronoi tessellations to scale up the multi-dimensional archive of phenotypic elites algorithm. IEEE Transactions on Evolutionary Computation. 2017 Aug 3.
4. Vassiliades V, Mouret JB. Discovering the Elite Hypervolume by Leveraging Interspecies Correlation. Proc. of GECCO. 2018.
5. Mouret JB, Maguire G. Quality Diversity for Multi-task Optimization. Proc of GECCO. 2020.
