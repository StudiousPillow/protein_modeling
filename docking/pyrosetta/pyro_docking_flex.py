import pyrosetta
from pyrosetta import pose_from_pdb, get_fa_scorefxn
from pyrosetta.rosetta.protocols.docking import DockingProtocol
from pyrosetta.rosetta.protocols.simple_moves import SwitchResidueTypeSetMover
from pyrosetta.rosetta.protocols.minimization_packing import PackRotamersMover
from pyrosetta.rosetta.core.pack.task import TaskFactory
from pyrosetta.rosetta.core.pack.task.operation import RestrictToRepacking, InitializeFromCommandline, IncludeCurrent
from pyrosetta.rosetta.core.scoring import ScoreFunctionFactory

# Initialize PyRosetta
pyrosetta.init()#extra_options="-ex1_threads 10"

# Load receptor and ligand
receptor = pose_from_pdb("receptor_min.pdb")
ligand = pose_from_pdb("ligand_min.pdb")

# Convert to full-atom mode
full_atom = SwitchResidueTypeSetMover("fa_standard")
full_atom.apply(receptor)
full_atom.apply(ligand)

# Create a docked pose by appending ligand to receptor
docked_pose = receptor.clone()
docked_pose.append_pose_by_jump(ligand, 1)

# Pre-pack the receptor-ligand complex
scorefxn = get_fa_scorefxn()
task_factory = TaskFactory()
task_factory.push_back(InitializeFromCommandline())
task_factory.push_back(RestrictToRepacking())

# task_factory.push_back(IncludeCurrent(True)) 

# Create a PackerTask from the TaskFactory
packer_task = task_factory.create_packer_task(docked_pose)

# Create the PackRotamersMover with the score function and PackerTask
pack_mover = PackRotamersMover(scorefxn, packer_task)

# Apply the packer to the docked pose
pack_mover.apply(docked_pose)

# Set up the docking protocol
# Set up and run the docking protocol
dock_prot = DockingProtocol()
dock_prot.set_lowres_scorefxn(ScoreFunctionFactory.create_score_function("interchain_cen"))
dock_prot.set_highres_scorefxn(scorefxn)

# Convert to centroid mode for low-res docking
centroid_mover = SwitchResidueTypeSetMover("centroid")
centroid_mover.apply(docked_pose)

# Run docking protocol
dock_prot.apply(docked_pose)

# Convert back to full-atom mode after docking
full_atom.apply(docked_pose)

# Regenerate the PackerTask after docking
packer_task = task_factory.create_packer_task(docked_pose)

# Create and apply the PackRotamersMover
pack_mover = PackRotamersMover(scorefxn, packer_task)
pack_mover.apply(docked_pose)

# Final minimization
min_mover = pyrosetta.rosetta.protocols.minimization_packing.MinMover()
min_mover.score_function(scorefxn)
min_mover.apply(docked_pose)

# Save the final docked structure
docked_pose.dump_pdb("docked_complex_flex2_min.pdb")

# Evaluate the final score
final_score = scorefxn(docked_pose)
print(f"Final docking score: {final_score}")