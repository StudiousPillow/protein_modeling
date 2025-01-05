# rmsf_to_bfactor.py
rmsf_file = "rmsf.xvg"
pdb_file = "average.pdb"
output_pdb = "rmsf_colored.pdb"

# Read RMSF values
with open(rmsf_file, "r") as f:
    rmsf_values = [float(line.split()[1]) for line in f if not line.startswith(('@', '#'))]

# Update PDB file with RMSF as B-factor
with open(pdb_file, "r") as pdb, open(output_pdb, "w") as out:
    res_idx = 0
    for line in pdb:
        if line.startswith("ATOM"):
            new_bfactor = f"{rmsf_values[res_idx]:.2f}"
            out.write(f"{line[:60]}{new_bfactor:>6}{line[66:]}")
            res_idx += 1
        else:
            out.write(line)
