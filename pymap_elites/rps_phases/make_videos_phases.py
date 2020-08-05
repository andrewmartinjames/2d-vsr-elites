# written by Andrew James
# converts archive file to videos of elites

import sys, os, subprocess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
import math
import map_elites.cvt as cvt_map_elites
import map_elites.common as cm_map_elites

def vsr_video(params, title):
    amp = params[0] * 10  # fits amp to [0,10]
    freq = params[1] * 10  # fits freq to [0,10]
    phase_list = []

    for count in range(2, len(params)):
        phase_list.append(params[count] * 720)  # fits phase to [0, 720]

    all_vox_string = ""
    for i in range(0, len(col_list)):
        for str_coord in col_list[i]:
            coords = str_coord.split(",")
            all_vox_string += str(coords[0]) + ',' + str(coords[1]) + ',' + str(amp) + ',' + str(
                freq) + ',' + str(phase_list[i]) + '\n'

    call_string = 'echo "' + all_vox_string + '" | java -cp 2dhmsr.jar it.units.erallab.hmsrobots.FineLocomotionStarter video ' + terrain + ' ' + init_pos + ' ' + sim_time + " " + title
    file = os.popen(call_string)
    return

def col_positions(ar_positions):
    col_list=[]
    copy_position=ar_positions.copy()
    to_remove = []
    for str_cord1 in ar_positions:
        cord1= str_cord1.split(",")
        col=[]
        for i in range (0,len(copy_position)):
            cord2= copy_position[i].split(",")
            if cord1[0]==cord2[0]:
                col.append(copy_position[i])
        for rm in col:
            copy_position.remove(rm)
        if len(col) > 0:
            col_list.append(col)
    return col_list

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
    global col_list
    col_list = col_positions(positions)

    archive = open(sys.argv[5])
    elites = archive.readlines()
    for elite in elites:
        io_str_list = elite.split(" ")
        params = []
        for i in range(5, len(io_str_list) - 1):
            params.append(float(io_str_list[i]))
        title = io_str_list[0]
        vsr_video(params, title)