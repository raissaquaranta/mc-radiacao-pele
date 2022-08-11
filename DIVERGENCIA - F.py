import pymcx as mcx

# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'

# Session initialization
cfg = mcx.create()
cfg["Session"]["Photons"] = 1e8

# Session parameters
cfg["Domain"]["Dim"] = [50, 100, 100]
cfg["Domain"]["LengthUnit"] = 0.1

cfg["Optode"]["Source"]["Type"] = "Disk"
cfg["Optode"]["Source"]["Pos"] = [50, 50, 50]

# Theoric divergences - Disk Source
# cfg["Optode"]["Source"]["Param1"] = [100, 0, 0, 0]
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -759.57]  # divergence in radian 15° = focal length 7.5957 mm
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -343.2]  # divergence in radian 60° = focal length 3.7320 mm
# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -57.73]  # divergence in radian 120° = focal length 0.5773 mm


# Girasol Divergences - Disk Source
cfg["Optode"]["Source"]["Param1"] = [17, 0, 0, 0]  # 1.7mm

# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -1545.4]  # theta 1

# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -1133.2]  # theta 2

# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -849.9]  # theta 3

# cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -629.5]  # theta 4

cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0, -499.8]  # theta 5


# Theoric divergences - Pencil Source
# cfg["Optode"]["Source"]["Param1"] = [0.2618, 0, 0, 0]  # divergence in radian 15°
# cfg["Optode"]["Source"]["Param1"] = [1.0472, 0, 0, 0]  # divergence in radian 60°
# cfg["Optode"]["Source"]["Param1"] = [2.0944, 0, 0, 0]  # divergence in radian 120°

#  Girasol Divergences - Pencil Source
# cfg["Optode"]["Source"]["Param1"] = [0.034, 0, 0, 0]  # divergence in HTM FLuence
# cfg["Optode"]["Source"]["Param1"] = [0.043, 0, 0, 0]  # divergence in Ibramed 14
# cfg["Optode"]["Source"]["Param1"] = [0.052, 0, 0, 0]  # divergence in Ibramed 11


cfg["Shapes"].pop()
cfg["Shapes"] = [{"Grid": {"Tag": 1, "Size": [50, 100, 100]}}]

cfg["Domain"]["Media"].pop()
# # 660 nm
# cfg["Domain"]["Media"].append({
#     "mua": 0.03316,
#     "mus": 8.55509,
#     "g": 0.91,
#     "n": 1.37})
#
# # 830 nm
# cfg["Domain"]["Media"].append({
#      "mua": 0.01006,
#      "mus": 7.34241,
#      "g": 0.91,
#      "n": 1.37
#  })

# 904 nm
cfg["Domain"]["Media"].append({
     "mua": 0.01038,
     "mus": 6.25059,
     "g": 0.91,
     "n": 1.37
 })

for i in range(5):
    # Changing session name
    # name = 'F-div-theta1-s' + str(i + 1)
    # name = 'F-div-theta2-s' + str(i + 1)
    # name = 'F-div-theta3-s' + str(i + 1)
    # name = 'F-div-theta4-s' + str(i + 1)
    name = 'F-div-theta5-s' + str(i + 1)
    cfg["Session"]["ID"] = name
    print(cfg["Session"]["ID"])
    # Running the simulation
    data_mch, data_mc2 = mcx.run(cfg=cfg, flag='--outputtype F --outputformat nii', mcxbin=mcx_local)



