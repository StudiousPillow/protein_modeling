import pyrosetta
from pyrosetta import pose_from_pdb, get_fa_scorefxn
from os import listdir, path
from pathlib import Path
import csv

pyrosetta.init()
print("starting")

def score_complex(pdb_file):
    # Load the PDB file into a pose object
    pose = pose_from_pdb(pdb_file)
    
    # Get the full-atom scoring function
    scorefxn = get_fa_scorefxn()
    
    # Score the complex
    score = scorefxn(pose)
    
    # Return the score (lower values indicate better binding)
    return score

pdb_file = "docked_complex_flex2_min.pdb"

print(score_complex(pdb_file))