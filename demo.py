### IMPORTS AND STATIC VARIABLES ###
from pathlib import Path
import pickle
from utils.esm2_encode import  get_esm2_encs, read_acc_seqs_from_fasta 

# set work directory this file's directory location
WORK_DIR = Path( Path(__file__).parent.resolve() )

### MAIN ###

# read fasta into list tuple format: (acc1, seq1), (acc2, seq2)...] 
example_fastafile = WORK_DIR / "example_proteins" / "example_proteins.fasta"
accs_seqs = read_acc_seqs_from_fasta(example_fastafile)

# create esm2 encodings list of tensors - same order fasta file [esm2_enc1, esm2_enc2...]
esm2_encs = get_esm2_encs(accs_seqs) 
with open(WORK_DIR / "example_proteins_esm2enc.pickle", "wb") as outfile: pickle.dump(esm2_encs, outfile) 
