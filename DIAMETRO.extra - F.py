import pymcx as mcx

# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'

# Session initialization
cfg = mcx.create()
cfg["Session"]["Photons"] = 1e8

# Session parameters
cfg["Domain"]["Dim"] = [50, 150, 150]
cfg["Domain"]["LengthUnit"] = 0.1

cfg["Optode"]["Source"]["Type"] = "Disk"  # disk to be able to add radius in voxels
cfg["Optode"]["Source"]["Pos"] = [50, 75, 75]

# cfg["Optode"]["Source"]["Param1"] = [15.9, 0, 0, 0]  # radius 1,59 mm
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, 0]
#
# cfg["Optode"]["Source"]["Param1"] = [20.8, 0, 0, 0]  # radius 2,08 mm
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, 0]

# cfg["Optode"]["Source"]["Param1"] = [34.6, 0, 0, 0]  # radius 3,46mm
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, 0]

# cfg["Optode"]["Source"]["Param1"] = [26.9, 0, 0, 0]  # radius 2,69mm in Ibramed-Antares 2
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -49.8148]

cfg["Optode"]["Source"]["Param1"] = [34.6, 0, 0, 0]  # radius 3,46mm in HTM-Fluence
cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -101.7647]

cfg["Shapes"].pop()
cfg["Shapes"] = [{"Grid": {"Tag": 1, "Size": [50, 150, 150]}}]

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
    name = 'F-HTMF-e8-s' + str(i+1)
    cfg["Session"]["ID"] = name
    print(cfg["Session"]["ID"])
    # Running the simulation
    data_mch, data_mc2 = mcx.run(cfg=cfg, flag='--outputtype F --outputformat nii', mcxbin=mcx_local)

