# 2dsoro
Connecting pymap_elites to 2d-VSR-Sim.

#### experiment.py:
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

#### Current in-use voxel parameter ranges:
1. Amplitude: [0,10]
2. Frequency: [0,10]
3. Phase: [-720,720]



## Citations
1. Medvet, Bartoli, De Lorenzo, Seriani. "[Design, Validation, and Case Studies of 2D-VSR-Sim, an Optimization-friendly Simulator of 2-D Voxel-based Soft Robots](https://arxiv.org/abs/2001.08617)" arXiv cs.RO: 2001.08617
2. Mouret JB, Clune J. Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909. 2015 Apr 20.
3. Vassiliades V, Chatzilygeroudis K, Mouret JB. Using centroidal voronoi tessellations to scale up the multi-dimensional archive of phenotypic elites algorithm. IEEE Transactions on Evolutionary Computation. 2017 Aug 3.
4. Vassiliades V, Mouret JB. Discovering the Elite Hypervolume by Leveraging Interspecies Correlation. Proc. of GECCO. 2018.
5. Mouret JB, Maguire G. Quality Diversity for Multi-task Optimization. Proc of GECCO. 2020.
