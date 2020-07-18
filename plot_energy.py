# Created on Sat Jul 11 2020
# Author: Nuwan Dewapriya

import numpy as np
import matplotlib.pyplot as plt

# variables
energy_time = []

# read dump file
with open("energy.dump") as f:
    data = f.readlines()

# split a string into a list    
for x in data[1:]:
    energy_time.append(x.split())

# assign values to the variables    
time = [energy_time[x][0] for x in range(0, len(energy_time))]
energy = [energy_time[x][1] for x in range(0, len(energy_time))]
    
# convert variables to float
time_flt = [float(i) if '.' in i else int(i) for i in time]
energy_flt = [float(i) if '.' in i else int(i) for i in energy]

# plot
fig = plt.figure()
plt.plot(np.asanyarray(time_flt), np.asanyarray(energy_flt), '-r', linewidth=2.0)
plt.xlabel('Time (Ps)', fontsize=16)
plt.ylabel('Energy (kcal/mol)', fontsize=16)
plt.xlim(0, 50)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()
fig.savefig('energy_time.png', dpi=300, bbox_inches = "tight")