#!/bin/bash
conda create -y --name ROexam python=3.7 &&
source ~/anaconda3/bin/activate ROexam &&
pip install --ignore-installed -r ./config/requirements.txt &&
pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install --user &&
conda deactivate
