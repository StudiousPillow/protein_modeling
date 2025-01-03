gmx pdb2gmx -f I-tasser.pdb
## charmm27 (8)
## TIP3P (1)
## wasn't asked 135 mM sodium
## wasn't asked intact disulfide bridges
## creates topol.top and conf.gro and posre.itp

## box
gmx editconf -f conf.gro -o box.gro -c -d 2.0 -bt dodecahedron
## -> box.gro

## solvent
gmx solvate -cp box.gro -cs spc216.gro -p topol.top -o solv.gro

#Output configuration contains 761789 atoms in 251473 residues
#Volume                 :     7778.12 (nm^3)
#Density                :     979.805 (g/l)
#Number of solvent molecules:  250875   

## ions
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr

#NOTE 1 [file ions.mdp]:
 # With Verlet lists the optimal nstlist is >= 10, with GPUs >= 20. Note
  #that with the Verlet scheme, nstlist has no effect on the accuracy of
  #your simulation.

#NOTE 2 [file topol.top, line 87664]:
 # System has non-zero total charge: 6.000000
  #Total charge should normally be an integer. See
  #https://manual.gromacs.org/current/user-guide/floating-point.html
  #for discussion on how close it should be to an integer.

#NOTE 3 [file ions.mdp]:
 # You are using a plain Coulomb cut-off, which might produce artifacts.
  #You might want to consider using PME electrostatics.
## -> mdout.mdp, ions.tpr

gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -neutral
## 13- SOL

#Number of (3-atomic) solvent molecules: 250875

## minimisation
gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr

gmx mdrun -v -deffnm em
## quite long

gmx energy -f em.edr -o potential.xvg
## 10. Coul.-recip.

## equilibrate and bring to temperature
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr

gmx mdrun -v -deffnm nvt
## quite long

gmx energy -f nvt.edr -o temperature.xvg
## 16 Conserved-En.

## same with pressure
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr

gmx mdrun -v -deffnm npt

gmx energy -f npt.edr -o pressure.xvg
## 18 Pres.-DC

gmx energy -f npt.edr -o density.xvg
## 24 Volume

######## here 

## run MD
gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr

nohup gmx mdrun -v -deffnm md_0_1 -nb gpu > mdrun_simulation.log


