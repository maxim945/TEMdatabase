# merger.py

from Bio import SeqIO
import os

def merge_fasta_files(input_dir, output_file):
    records = []

    for file in os.listdir(input_dir):
        if file.endswith(".fasta"):
            with open(os.path.join(input_dir, file), "r") as f:
                records += list(SeqIO.parse(f, "fasta"))

    with open(output_file, "w") as f:
        SeqIO.write(records, f, "fasta")
