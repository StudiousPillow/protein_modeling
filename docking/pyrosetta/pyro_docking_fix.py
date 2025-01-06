import pyrosetta
from pyrosetta import pose_from_pdb, get_fa_scorefxn
from pyrosetta.rosetta.protocols.docking import DockingProtocol
from pyrosetta.rosetta.protocols.simple_moves import SwitchResidueTypeSetMover
from pyrosetta.rosetta.protocols.rigid import RigidBodyTransMover

# Initialize PyRosetta
pyrosetta.init()

# Load receptor and ligand
receptor = pose_from_pdb("receptor.pdb")
ligand = pose_from_pdb("ligand.pdb")

# Convert to full-atom mode initially
full_atom = SwitchResidueTypeSetMover("fa_standard")
full_atom.apply(receptor)
full_atom.apply(ligand)

# Create a docked pose by appending ligand to receptor
docked_pose = receptor.clone()
docked_pose.append_pose_by_jump(ligand, 1)

# Move the ligand closer to the receptor to avoid rejected moves
rigid_body_mover = RigidBodyTransMover(docked_pose, 1)
rigid_body_mover.step_size(5.0)  # Adjust step size if needed
rigid_body_mover.apply(docked_pose)

# Set up the docking protocol
dock_prot = DockingProtocol()

# Define low-res (centroid) and high-res (full-atom) scoring functions
lowres_scorefxn = pyrosetta.create_score_function('interchain_cen')  # Low-res scoring
highres_scorefxn = get_fa_scorefxn()  # High-res scoring

# Set the docking protocol scoring functions
dock_prot.set_lowres_scorefxn(lowres_scorefxn)
dock_prot.set_highres_scorefxn(highres_scorefxn)

# Convert pose to centroid mode for low-res docking
centroid_mover = SwitchResidueTypeSetMover("centroid")
centroid_mover.apply(docked_pose)

# Run the docking protocol
dock_prot.apply(docked_pose)

# Convert back to full-atom mode after docking
full_atom.apply(docked_pose)

# Save the final docked structure
docked_pose.dump_pdb("docked_complex_min.pdb")

# Evaluate the final score
score = get_fa_scorefxn()(docked_pose)
print(f"Final docking score: {score}")