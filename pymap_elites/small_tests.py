import sys, os, subprocess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#DATA format in TRAVEL_X_VELOCITY,
# TRAVEL_X_RELATIVE_VELOCITY,
# CENTER_AVG_Y,
# CONTROL_POWER ,
# RELATIVE_CONTROL_POWER
import numpy as np

def vsr_simulate():

    ##### UNDER CONSTRUCTION #####
    file = os.popen(
        'echo 0,0,1,1,1 | java -cp ../2d-vsr-sim/2dhmsr.jar it.units.erallab.hmsrobots.FineLocomotionStarter summary 1,0:1000,100:2000,10 1 10'
    )
    string_of_file = file.read()
    arrSplited_matrices=string_of_file.split(",\n")
    dataArr=[]
    dictMetrice={}
    for metric in arrSplited_matrices:
        key_valueMetric=metric.split("=")
        dictMetrice[key_valueMetric[0]]=float(key_valueMetric[1])

    dataArr.append(dictMetrice.get("DELTA_X"))
    dataArr.append(dictMetrice.get("INTEGRAL_Y"))
    dataArr.append(dictMetrice.get("INTEGRAL_Theta"))
    return dictMetrice.get("ABS_INTEGRAL_X"), np.array(dataArr)


print(vsr_simulate())
