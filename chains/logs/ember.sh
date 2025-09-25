#!/bin/bash -l
#$ -cwd
#$ -V
#$ -N ember
#$ -o logs/$JOB_NAME.$JOB_ID.$TASK_ID.out
#$ -e logs/$JOB_NAME.$JOB_ID.$TASK_ID.err
#$ -t 1-2048

set -euo pipefail
module load miniconda


echo "Host: $(hostname)"
echo "Job:  $JOB_NAME  ID: $JOB_ID  Task: $SGE_TASK_ID"
echo "Cmd:  ember fit-sed /project/mesaelm/omnidwarf/GaiaDR3_white_dwarfs.pqt /project/mesaelm/omnidwarf/chains/ --xpphoto --synthetic --mcmc --source-id GaiaEDR3 --ra RA_ICRS --dec DE_ICRS --parallax PlxZPCorr --parallax-error e_Plx --meanav meanAV --numtasks 2048"

# Run the command
ember fit-sed /project/mesaelm/omnidwarf/GaiaDR3_white_dwarfs.pqt /project/mesaelm/omnidwarf/chains/ --xpphoto --synthetic --mcmc --source-id GaiaEDR3 --ra RA_ICRS --dec DE_ICRS --parallax PlxZPCorr --parallax-error e_Plx --meanav meanAV --numtasks 2048
