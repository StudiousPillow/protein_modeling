import sys

# Read RMSF values from rmsf.xvg
with open('rmsf_res.xvg') as rmsf_file:
    rmsf_values = [float(line.split()[1]) for line in rmsf_file if not line.startswith(('#', '@'))]

# Read PDB file
pdb_file = 'average_structure.pdb'
with open(pdb_file) as pdb:
    pdb_lines = pdb.readlines()

# Write new PDB file with RMSF values as B-factors
res_index = 0
with open('rmsf_colored.pdb', 'w') as output:
    for line in pdb_lines:
        if line.startswith('ATOM'):
            if res_index < len(rmsf_values):
                new_line = f"{line[:60]}{rmsf_values[res_index]:6.2f}{line[66:]}"
                res_index += 1
            else:
                new_line = f"{line[:60]}{0.00:6.2f}{line[66:]}"
            output.write(new_line)
        else:
            output.write(line)
