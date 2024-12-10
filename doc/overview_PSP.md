https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2023.1120370/full
-> we don't have novel, so TBM thread/fold if there are similar prot, or langage model
-> ESMFold, (EMBER), GenTHREADER (old)
https://en.wikipedia.org/wiki/List_of_protein_structure_prediction_software
-> décevant
https://pubs.acs.org/doi/10.1021/acs.jcim.4c01598
-> pas accès, int
https://github.com/A4Bio/ProteinInvBench
-> à lire 
https://proteinbench.github.io/
-> à lire 
https://www.sciencedirect.com/science/article/pii/S0300908420300961
-> bien à relire 
https://tbiomed.biomedcentral.com/articles/10.1186/s12976-015-0014-1
-> good explaination but not up to date (2015)
https://pubmed.ncbi.nlm.nih.gov/36926275/
https://pubmed.ncbi.nlm.nih.gov/38761500/
-> alphafold2 limits
https://github.com/Peldom/papers_for_protein_design_using_DL
https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00045a
https://torchprotein.ai/benchmark#leaderboard-for-secondary-structure-prediction
-> for AI, ESM-1b is best (and with contact even better)

### Physics
- [Meld](https://github.com/maccallumlab/meld) in [2016](https://www.scopus.com/record/display.uri?eid=2-s2.0-85018198432&origin=inward&txGid=4f42274e2ad2bd922f100a7661b363ed)
maintained
physics-based, Bayesian framework
requires GPU (otherwise very slow)
"the typical inputs to MELD are (i) the protein sequence, (ii) predicted secondary structures from PSIPRED (23), and (iii) externally supplied information about residue–residue contacts or distances"
so not just the protein sequence

### Langage neural network
- [OmegaFold](https://github.com/HeliXonProtein/OmegaFold) in [2022](https://www.biorxiv.org/content/10.1101/2022.07.21.500999v1.full.pdf+html)
doesn't seem maintained, but quite used
Works with only the protein sequence, adapted to work on "orphan proteins"
"large pretrained language model for sequence modeling and a geometry-inspired transformer
model for structure prediction"
- [FoldingDiff](https://github.com/microsoft/foldingdiff) in [2022](https://arxiv.org/abs/2209.15611) and [2024](https://www.nature.com/articles/s41467-024-45051-2)
2 years ago but a bit maintained ? plus microsoft
diffusion ?
- [SPIRED](https://github.com/Gonglab-THU/SPIRED-Fitness) 
https://www.nature.com/articles/s41467-024-51776-x
- [ESMFold](https://github.com/facebookresearch/esm) https://www.biorxiv.org/content/10.1101/622803v4
facebook ?
langage transformer model
why archived ? New repo ?
very good for novel strucures
- [RosettaFold](https://github.com/RosettaCommons/RoseTTAFold) https://github.com/RosettaCommons/RoseTTAFold
Performer(?) neural network with 3 tracks(?)
- [DMPFold2](https://github.com/psipred/DMPfold2) https://www.pnas.org/content/119/4/e2113348119


not open source
- [ModFold9](https://www.sciencedirect.com/science/article/pii/S0022283624001189) to estimate quality of 3D structure.
- https://www.cameo3d.org/
- [MaxCluster](https://www.sbg.bio.ic.ac.uk/~maxcluster/index.html) to compare different proteins
- [Modeller](https://salilab.org/modeller/)
only for homology
- [RaptorX] website doesn't work it is so old

à checker
SwissModel,I-Tasser,Rosetta
helixfoldsingle
trRosettaX-single
RGN2
HelixFold
Helix Fold-single
PPI3D
molbio tools ca
LSCF bioinfo weizmann
COSMIC2

The [RCSB](https://www.rcsb.org/docs/additional-resources/structure-prediction) is a good starting point. 
-> OpenFold, HelixFold, Helix Fold-single

# Other
iCn3D -> visualisation uniquement
https://www.ncbi.nlm.nih.gov/Structure/icn3d/icn3d.html


ModelArchive (theoretical models tocheck)

ModBase

MMDB ? molecular modelling db
VAST ?

- [Deepfold](https://github.com/robpearc/DeepFold)
https://zhanggroup.org/DeepFold/
not maintained
- [DeepFRI](https://github.com/flatironinstitute/DeepFRI)
not really maintained
- [protein-glue](https://github.com/ibivu/protein-glue)
https://www.nature.com/articles/s41598-022-19608-4

https://pmc.ncbi.nlm.nih.gov/articles/PMC10874569/?
https://pmc.ncbi.nlm.nih.gov/articles/PMC8828571/?
https://www.uniprot.org/uniprotkb/Q6P1W5/publications
