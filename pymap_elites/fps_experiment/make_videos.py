# written by Andrew James
# converts archive file to videos of elites

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def vsr_video(params, title):
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

    call_string = 'echo "' + all_vox_string + '" | java -cp 2dhmsr.jar it.units.erallab.hmsrobots.FineLocomotionStarter video ' + terrain + ' ' + init_pos + ' ' + sim_time + " " + title
    file = os.popen(call_string)
    return

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

    archive = open(sys.argv[5])
    elites = archive.readlines()
    for elite in elites:
        io_str_list = elite.split(" ")
        params = []
        for i in range(5, len(io_str_list) - 1):
            params.append(float(io_str_list[i]))
        title = io_str_list[0]
        vsr_video(params, title)