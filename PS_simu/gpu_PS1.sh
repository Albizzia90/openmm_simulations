#!/bin/bash
#SBATCH --job-name="PS"
#SBATCH --time=24:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=1   # 36 processor core(s) per node
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu    # gpu node(s)

module purge
module load cuda

source ~/.bashrc
source activate /work/LAS/potoyan-lab/sean/miniconda3/envs/llpsmd_Jun_nuc   # change this path to your install path of conda environment

python PS1.py
