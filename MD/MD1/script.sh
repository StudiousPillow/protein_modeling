gmx pdb2gmx -f Q6P1W5.pdb
## charmm27 (8)
## TIP3P (1)
## creates topol.top and conf.gro and posre.itp

## box
gmx editconf -f conf.gro -o box.gro -c -d 2.0 -bt dodecahedron
## creates box.gro

## solvent
gmx solvate -cp box.gro -cs spc216.gro -p topol.top -o solv.gro

#Output configuration contains 761789 atoms in 251473 residues
#Volume                 :     7778.12 (nm^3)
#Density                :     979.805 (g/l)
#Number of solvent molecules:  250875   

## ions
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr
## creates mdout.mdp, ions.tpr

gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -neutral
## choose 13- SOL

#Number of (3-atomic) solvent molecules: 250875

## minimisation
gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -v -deffnm em
gmx energy -f em.edr -o potential.xvg
## choose 10. Coul.-recip.

## equilibrate and bring to temperature
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
gmx mdrun -v -deffnm nvt

gmx energy -f nvt.edr -o temperature.xvg
## choose 16 Conserved-En.

## same with pressure
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
gmx mdrun -v -deffnm npt
gmx energy -f npt.edr -o pressure.xvg
## choose 18 Pres.-DC

gmx energy -f npt.edr -o density.xvg
## choose 24 Volume

######## here 

## run MD
gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr
nohup gmx mdrun -v -deffnm md_0_1 > mdrun_simulation.log


