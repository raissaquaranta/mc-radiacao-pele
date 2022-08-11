# This code is the first try to simulate a media with multiple layers with different
# optical properties. It worked making the differences between the layers greater.

import pymcx as mcx
import matplotlib.pyplot as plt
import nibabel as nii
import numpy as np
import seaborn as sns


# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'

# Session initialization
cfg = mcx.create()
cfg["Session"]["Photons"] = 1e8

# Session parameters
cfg["Domain"]["Dim"] = [50, 100, 100]
cfg["Domain"]["LengthUnit"] = 0.1

cfg["Optode"]["Source"]["Type"] = "Disk"
cfg["Optode"]["Source"]["Param1"] = [17, 0, 0, 0]
cfg["Optode"]["Source"]["Pos"] = [50, 50, 50]
cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0]

cfg["Shapes"].pop()
cfg["Shapes"] = [{"Grid": {"Tag": 1, "Size": [50, 100, 100]}}]
cfg["Shapes"].append({"XLayers": [[0, 19, 2]]})  # muscle
cfg["Shapes"].append({"XLayers": [[20, 34, 3]]})  # fat

cfg["Domain"]["Media"].pop()
# 904 nm
cfg["Domain"]["Media"].append({
     "mua": 0.01038,
     "mus": 6.25059,
     "g": 0.91,
     "n": 1.37
 })

# Muscle optical properties Tag 2
cfg["Domain"]["Media"].append({
     "mua": 0.3339,
     "mus": 9.0322,
     "g": 0.930,
     "n": 1.37})

# Fat optical properties Tag 3
cfg["Domain"]["Media"].append({
     "mua": 0.323,
     "mus": 10.2361,
     "g": 0.9,
     "n": 1.44})


# Multiple sessions block
for i in range(5):
    # Changing session name
    name = 'F-904-3-LAYERS-s' + str(i+1)
    cfg["Session"]["ID"] = name
    print(cfg["Session"]["ID"])
    # Running the simulation
    data_mch, data_mc2 = mcx.run(cfg=cfg, flag='--outputtype F --outputformat nii', mcxbin=mcx_local)

