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

pdb_path = "complex_pdb"
output_score_file = "scores.csv"

# Get all pdb files
pdb_files = [path.join(pdb_path, f) for f in listdir(pdb_path) if path.isfile(path.join(pdb_path, f))]

out = open(output_score_file, 'w')
scores = {}
writer = csv.writer(out)
writer.writerow(["PDBFile", "Score"])

for pdb_file in pdb_files:
    print(pdb_file)
    pdbname = Path(pdb_file).stem
    score = score_complex(pdb_file)
    scores[pdbname] = score
    print(f"Score for {pdb_file}: {score}")
    writer.writerow([pdbname, score])

best_complex = min(scores, key=scores.get)
print(f"Best complex: {best_complex} with score: {scores[best_complex]}")

out.close()