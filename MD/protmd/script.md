## fix the pdb file (hydrogens, charges, protonation, other?) and generate files for martini coarse grained model and force field
```bash
pdbfixer model_itasser.pdb --output complex.pdb 
martinize2 -f complex.pdb -x cg.pdb -o topol.top -ff martini3001
```
molecule_0.itp
cg.pdb
topol.top

Modify topol.top to add the .itp files and remove martini.itp
#include "martini_v3.0.0.itp"
#include "martini_v3.0.0_ions_v1.itp"
#include "martini_v3.0.0_solvents_v1.itp"

Careful to put them in this order.

## add the box to the structure
```bash
gmx editconf -f cg.pdb -o box.gro -c -d 2.0 -bt dodecahedron
```
box.gro

## add the solvent to the structure
```bash
gmx solvate -cp box.gro -cs water.gro -p topol.top -o solv.gro 
```
solv.gro

## add the ions so that the total charge is 0 

```bash
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr --maxwarn 4
```
ions.tpr
```bash
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -neutral
```
select 13 water
solv_ions.gro

## small md to test the performance

topol.tpr

```bash
gmx grompp -f mdtest.mdp -c solv_ions.gro -p topol.top -o testmd.tpr
```
gmx mdrun -gpu_id 0 -s testmd.tpr
```bash
gmx mdrun -v -deffnm testmd -nb gpu
```
or
```bash
nohup gmx mdrun -v -deffnm testmd -nb cpu > testmd.out
```

## minimisation (small MD) -> here GPU ?
```bash
gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -v -deffnm em
```

gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
gmx mdrun -v -deffnm nvt



gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
gmx mdrun -v -deffnm npt


gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr
nohup gmx mdrun -v -deffnm md_0_1 -nb cpu > mdrun_simulation.log
