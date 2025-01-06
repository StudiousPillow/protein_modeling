cd raw_complex
for pdb in *.pdb
do
	echo $pdb
	echo "../pdbqt/${pdb/.pdb/.pdbqt}"
	pythonsh ../prepare_receptor4.py -r $pdb -A hydrogens -U nphs_lps_waters -v -o ../pdbqt/${pdb/.pdb/.pdbqt}
done

