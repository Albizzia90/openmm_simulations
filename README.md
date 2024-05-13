# Openmm_simulations
basic notes on phase separation, viscosity, contact analysis for bio-condensates

# Installation
## Install Homebrew and Anaconda environment in a Mac
follow the steps in the [link](https://gist.github.com/ryanorsinger/7d89ad58901b5590ec3e1f23d7b9f887)
## Install packages for openmm
```
conda create -n llpsmd_env python=3.9 numpy scipy pandas matplotlib
conda activate llpsmd_env     # 'llpsmd_env' is the name of the environment, can be changed by yourself
    # after that, you could see an environment named as 'llpsmd_env' in VS code
conda install -c conda-forge openmm mdtraj parmed mbuild packmol foyer
conda install -c conda-forge cudatoolkit=11.4     # cudatoolkit for gpu calculation
    # the version of cudatoolkit maybe inavailable. If you only use cpu, 'cudatoolkit' is not necessary.
```
install [openmm package](https://github.com/PotoyanGroup/llpsmd) from Davit Potoyan, follow the README instruction.
Sometimes, the version of ipywidgets need to be adjusted,
```
pip install ipywidgets==7.6.5  
```
check the install by
```
python ./tests/test_omm_nvt.py
```

# Phase separation (PS) simulation

## Slab initialization
see the folder 'PS_init'

## Run the simulation
see ipynb & py files in the folder 'PS_simu'

## Analyze the results (files in 'PS_analyze')
After a simulation, we first show its trajectory to estimate its physical properties. The trajectory can be displayed by software, like Ovito, pyMol; or using python package (mdtraj, mdanalysis). 
For phase diagram, we mainly need to judge if PS happened and if the two phases (dilute and dense phases) are clear enough to analyze. In one round of simulations, find out the highest temperature that PS exists; then do another simulation round with smaller temperature step near this temperature. Repeat this process several times until you get the temperature close enough to the critical temperature.

To get the density profile, make the density centralized in the slab for each frame, then accumlate the density profiles to get the average profile. This process is shown in 'densityProfile.ipynb'

Use tanh function to fit the average density profile and get the dilute and dense density. The code is shown in 'densityProfile.ipynb'
![alt text](https://github.com/Albizzia90/openmm_simulations/blob/main/PS_analyze/densZ_fit.png?raw=true)

Near the critical temperature, record about 5 pairs of temperature-density data points, fit to get the critical temperature and density. The process is shown in 'phaseDiagram.ipynb'
![alt text](https://github.com/Albizzia90/openmm_simulations/blob/main/PS_analyze/phaseDiag_dens.png?raw=true)
# *Viscosity (todo)


