## Introduction
This repositiory is guide for installing and using the protein language model (PLM) ESM2.
## Installation
To install ESM2 you will need a python installation. 
For easy GPU utilizaiton, we will use python within conda. Conda can be installed from here: https://docs.anaconda.com/miniconda/install/ 
### Create conda environment
```
$ conda create -n esm2 # create conda virtual environment
$ conda install numpy
$ conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia # install pytorch with gpu support
$ pip install fair-esm # install esm source with pip
```
### Clone this repo
```
$ git clone https://github.com/mnielLab/esm2_utilities.git
```
### Creating sequence encodings
```
Source code for encoding sequence batches is included in ./utils/esm2_encode.py
A use-case example of creating ESM2 encodings example sequences in the fasta file ./example_proteins/example_proteins.fasta is included in ./demo.py.
To run this example,
$ python demo.py
```
