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

# Phase separation simulation

## Slab initialization
see the folder 'PS_init'

## Run the simulation
see ipynb & py files in the folder 'PS_simu'

## Analyze the results
see the folder 'PS_analyze'

# *Viscosity (todo)


