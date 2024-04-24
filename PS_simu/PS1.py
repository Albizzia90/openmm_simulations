from llpsmd.utils import load_parmed
from llpsmd.omdsim import OMDSim
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

### parameters, need to change for your file names
NTag= 'M700x14'
Temp= 300
TTag= f'T{Temp}'
folder= './'+TTag+NTag

###
print(folder)
if not os.path.exists(folder):
    os.makedirs(folder)

pmd = load_parmed(fname=folder+'/packInit_'+NTag)
print(pmd.topology)

###
mysim = OMDSim(pmd, param= 'M2', device= 'CUDA') # device= 'CUDA', ?fname= ?
mysim.add_dh_force(ionic=0.1, temp=Temp,  n_excl=1, r_cut=4)
mysim.add_lj_lambda(eps=0.8368, n_excl=1, r_cut=4)

print('add external force, k=0.01')
mysim.add_external(k=0.01)
mysim.run_nvt(temp=Temp, gamma=0.01, dt=0.01, minimize=True, n_steps=100000, log_step=5000, fname=folder+'/attract')

print('remove external force...')
mysim.remove_external()
mysim.run_nvt(temp=Temp, gamma=0.01, dt=0.01, minimize=False, n_steps=50000000, log_step=5000, fname=folder+'/output')
