# fwf-lrf-processing
This repository contains the pre-processing, coupling and initial analysis code for the EC-Earth freshwater forcing emulation code, (but does not include any changes that need to be made within EC-Earth). As the code was directly copied from various directories, there are some duplicate bits of code and some which may no longer be relevant. 

## Pre-processing
Create nc file of runoff masks for Antarctica

## Scripts
Freshwater coupling scripts
- `scripts/create_fwf_y1850.ipynb` creates fwf for 1850, I don't think this is used in the coupling process. 
- `scripts/InitialiseFreshwaterForcing.py` Initialise freshwater forcing experiment by creating initial freshwater forcing file and depth distribution files
- `scripts/PrescribedFreshwaterForcing.py` Prescribed freshwater, for non-interactive experiments?
- `scripts/ThetaoDrivenFreshwaterForcing.py` Compute Antarctic freshwater forcing anomalies from ocean subsurface temperature in 5 regions

`BasalMelt.py, FreshWaterForcing.py and DataVariablesForcing.py` are functions associated with the scripts. 

## Analysis
