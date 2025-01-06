import pyrosetta
from pyrosetta import pose_from_pdb, get_fa_scorefxn
from pyrosetta.rosetta.protocols.minimization_packing import MinMover

pyrosetta.init()

def score_pose(pose):
    # Get the full-atom scoring function
    scorefxn = get_fa_scorefxn()
    
    # Score the complex
    score = scorefxn(pose)
    
    # Return the score (lower values indicate better binding)
    return score

def minimise_pose(pose):
    min_mover = MinMover()
    min_mover.score_function(get_fa_scorefxn())
    # Perform minimization on the receptor pose
    min_mover.apply(pose)
    return(pose)

pdb_file = "model.004.18.pdb"

# Load the PDB file into a pose object
model = pose_from_pdb(pdb_file)

score_before = score_pose(model)
print(f'score_before: {score_before}')

model_min = minimise_pose(model)

score_after = score_pose(model_min)
print(f'score_after: {score_after}')

model_min.dump_pdb("cluspro_bestcomplex_min.pdb")