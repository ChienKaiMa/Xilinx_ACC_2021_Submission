import numpy as np
from scipy.io import mmread

with open('temp_task.txt', 'r') as f:
    a = mmread(f)

# Calculation result from AWS SBM in ising mode with the above file 'temp_taxk.txt':
# "value": -4.76837158203125e-7
# "result":
state = np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1])
# We set these parameters ourselves: steps=3600, dt=0.01

# Local energy value calculation result
energy_local = a.dot(state).dot(state)
print(energy_local)
# 1.726549214708939e-07

energy_local_32 = a.astype(np.float32).dot(state).dot(state)
print(energy_local_32)
# -9.5367431640625e-07