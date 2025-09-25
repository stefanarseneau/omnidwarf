## OMNIDWARF

Fit all the white dwarfs!

This repository does parameter estimation on all the white dwarfs in Gentile-Fusillo+2021 that have XP spectra using the `ember` code. To run:

```
ember submit fit-sed /project/mesaelm/omnidwarf/GaiaDR3_white_dwarfs.pqt /project/mesaelm/omnidwarf/chains/ --xpphoto --synthetic --mcmc --source-id GaiaEDR3 --ra RA_ICRS --dec DE_ICRS --parallax PlxZPCorr --parallax-error e_Plx --meanav meanAV --numtasks 256
```
