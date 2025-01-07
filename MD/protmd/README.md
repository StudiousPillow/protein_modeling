Test of gromacs simulation of the I-Tasser model with :
- Martini3 coarse-grained
- 10ps
- make it work on cpu 
- then test it on GPU 



.gro	Structure file	npt.gro
.top	Topology file	topol.top
.itp	Include topology file	martini_v3.0.itp
.mdp	Simulation parameter file	md.mdp
.tpr	Run input file	md.tpr
.xtc	Compressed trajectory file	md.xtc
.trr	Full-precision trajectory file	md.trr
.edr	Energy file	md.edr
.log	Log file	md.log
.cpt	Checkpoint file	state.cpt
.xvg	Graph file	rmsd.xvg