### IMPORTS ###
import sys
from pathlib import Path
import pickle
import torch
import esm
import numpy as np

def get_esm2_encs(data):
    """
    Compute per residue esm2 representation  
    
    input: data: list of tuples: [(seq_name, sequence)...]
    output: sequence_representations: list of esm2 torch tensors, same order data: [esm2_enc1, esm2_enc2...]  
    
    """


    # load ESM-2 model
    model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
    batch_converter = alphabet.get_batch_converter()
    model.eval()
    batch_labels, batch_strs, batch_tokens = batch_converter(data)
    batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)
    
    # extract per-residue representations
    with torch.no_grad(): results = model(batch_tokens, repr_layers=[33])
    token_representations = results["representations"][33]
    print(f"ESM-2 representation size of sequence batch with padding: {token_representations.size()}")
    
    # omitting embedding from padding, as well as start and end tokens
    sequence_representations = []
    for i, tokens_len in enumerate(batch_lens):
        batch_token = batch_tokens[i]
        # if there is cls, eos or padding token, exclude them
        if batch_token[0] == alphabet.cls_idx and (batch_token[-1] == alphabet.eos_idx or batch_token[-1] == alphabet.padding_idx):
            sequence_representations.append(token_representations[i, 1 : tokens_len - 1])
        # if not just add as is             
        else: sequence_representations.append(token_representations[i, :, :])

    for s in sequence_representations: print(f"ESM-2 representation size of sequence  after removing padding: {s.size()}") 

    return sequence_representations

def read_acc_seqs_from_fasta(infile_path):
    """
    input: readfile: Fasta file. Pathlib 
    output: accs_and_sequences: List of tuples. Containing accs and sequences, e.g. [(acc, aTHNtem..)..()].
    """
    accs = list()
    sequences = list()
    seq = ""
    read_acc = False

    infile = Path(infile_path)
    if not infile.is_file():
        print(f"The input file was invalid. Invalid file was {infile}")

    infile = open(infile, "r")
    readfile = infile.readlines()
    infile.close()

    for line in readfile:
        line = line.strip()
        if line.startswith(">"):
            acc = line.split(">")[1]
            if read_acc:
                accs.append(acc)
                sequences.append(seq)
                #reset sequence string
                seq = ""
            #catch first accesion.
            else:
                accs.append(acc)
        else:
            seq += line
            read_acc = True

    #get last sequence
    sequences.append(seq)
    accs_and_sequences = tuple( zip(accs, sequences) )
    return accs_and_sequences
