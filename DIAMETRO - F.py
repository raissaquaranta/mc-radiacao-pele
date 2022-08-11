import pymcx as mcx

# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'

# Session initialization
cfg = mcx.create()
cfg["Session"]["Photons"] = 1e8

# Session parameters
cfg["Domain"]["Dim"] = [50, 150, 150]
cfg["Domain"]["LengthUnit"] = 0.1

cfg["Optode"]["Source"]["Type"] = "Disk"  # disk to be abble to add radius in voxels
# Theoric radius
# cfg["Optode"]["Source"]["Param1"] = [50, 0, 0, 0]  # radius 0,5mm
# cfg["Optode"]["Source"]["Param1"] = [100, 0, 0, 0]  # radius 1,0mm
# cfg["Optode"]["Source"]["Param1"] = [200, 0, 0, 0]  # radius 2,0mm

#  Girasol radius
cfg["Optode"]["Source"]["Pos"] = [50, 75, 75]
cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0]
# cfg["Optode"]["Source"]["Param1"] = [9.1, 0, 0, 0]  # radius 0,91mm
# cfg["Optode"]["Source"]["Param1"] = [14.1, 0, 0, 0]  # radius 1,41mm
# cfg["Optode"]["Source"]["Param1"] = [20.8, 0, 0, 0]  # radius 2,08mm
# cfg["Optode"]["Source"]["Param1"] = [26.9, 0, 0, 0]  # radius 2.69mm
cfg["Optode"]["Source"]["Param1"] = [34.6, 0, 0, 0]  # radius 3.46mm


# cfg["Optode"]["Source"]["Param1"] = [158, 0, 0, 0]  # radius 1,58mm in Ibramed-Laser Pulse 1
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -58.5185]

# cfg["Optode"]["Source"]["Param1"] = [269, 0, 0, 0]  # radius 2,69mm in Ibramed-Antares 2
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -49.8148]

# cfg["Optode"]["Source"]["Param1"] = [346, 0, 0, 0]  # radius 3,46mm in HTM-Fluence
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -101.7647]


cfg["Shapes"].pop()
cfg["Shapes"] = [{"Grid": {"Tag": 1, "Size": [50, 150, 150]}}]

cfg["Domain"]["Media"].pop()
# # 660 nm Ibramed-Laser Pulse 1
# cfg["Domain"]["Media"].append({
#     "mua": 0.03316,
#     "mus": 8.55509,
#     "g": 0.91,
#     "n": 1.37})

# # 830 nm Ibramed-Antares 2
# cfg["Domain"]["Media"].append({
#      "mua": 0.01006,
#      "mus": 7.34241,
#      "g": 0.91,
#      "n": 1.37
#  })

# 904 nm HTM-Fluence
cfg["Domain"]["Media"].append({
     "mua": 0.01038,
     "mus": 6.25059,
     "g": 0.91,
     "n": 1.37
 })

for i in range(5):
    # Changing session name
    # name = 'F-r1-s' + str(i+1)
    # name = 'F-r2-s' + str(i + 1)
    # name = 'F-r3-s' + str(i + 1)
    # name = 'F-r4-s' + str(i + 1)
    name = 'F-r5x-s' + str(i + 1)
    cfg["Session"]["ID"] = name
    print(cfg["Session"]["ID"])
    # Running the simulation
    data_mch, data_mc2 = mcx.run(cfg=cfg, flag='--outputtype F --outputformat nii', mcxbin=mcx_local)