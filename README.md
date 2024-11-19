## Introduction
This repositiory is a guide for installing and making sequence encodings using the protein language model (PLM) ESM2.
## Installation
To install ESM2 you will need a python installation. 
For easy GPU utilizaiton, we will use python within conda. Conda can be installed from here: https://docs.anaconda.com/miniconda/install/ 
### Create conda environment
```
$ conda create -n esm2 # create conda virtual environment
$ conda activate esm2
$ conda install numpy
$ conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia # install pytorch with gpu support
$ pip install fair-esm # install esm source with pip
```
### Clone this repo
```
$ git clone https://github.com/mnielLab/esm2_utilities.git
```
### Creating sequence encodings
Source code for encoding sequence batches is included in ./utils/esm2_encode.py
A demo script for creating ESM2 encodings for sequences in an example fasta file is included in ./demo.poy
To run this example,
```
$ python demo.py
```
This will create per residue encodings for all sequences in ./example_proteins/example_proteins.fasta.
And save them in a .pickle formatted file, ./example_proteins_esm2enc.pickle
