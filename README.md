# fwf-lrf-processing
This repository contains the pre-processing, coupling and initial analysis code for the EC-Earth freshwater forcing emulation code, (but does not include any changes that need to be made within EC-Earth). As the code was directly copied from various directories, there are some duplicate bits of code and some which may no longer be relevant. 

## Pre-processing
Create nc file of runoff masks for Antarctica

## Scripts
Inputs needed for running:
- area file
- a basal melt mask: created in pre-processing
- a calving mask: created in pre-processing
- basal melt depth1 & 2 files: this is the shallowest and deepest depths that the basal melt is calculated over. I do not know how these files are created. 
- FriverDistributionMask_AIS_ORCA1.nc: I think this is no longer used and has now been replaced by separate basal melt and calving masks.
- Baseline thetao file from control run
- Total freshwater averaged over a certain period (to calculate anomalies).
- Cumulative future freswater file for linear response function (this is an estimate from the ice sheet model)

Freshwater forcing scripts:
- `scripts/create_fwf_y1850.ipynb` creates fwf for 1850, I don't think this is used in the coupling process. 
- `scripts/InitialiseFreshwaterForcing.py` Initialise freshwater forcing experiment by creating initial freshwater forcing file and depth distribution files. The initial freshwater file needs to be present before the run starts. 
- `scripts/PrescribedFreshwaterForcing.py` Prescribed freshwater, used for doing the control experiment
- `scripts/ThetaoDrivenFreshwaterForcing.py` Compute Antarctic freshwater forcing anomalies from ocean subsurface temperature in 5 regions, this is used for the interactive freshwater forcing.

`BasalMelt.py, FreshWaterForcing.py and DataVariablesForcing.py` are functions associated with the scripts. 

The code is called at the bottom of `ece-esm.sh.tmpl` as fwf=4 and calls `fwfwrapper.sh`. 
`fwfwrapper.sh` calls either `scripts/ThetaoDrivenFreshwaterForcing.py` for interactive fwf or `scripts/ThetaoDrivenFreshwaterForcing.py` for prescribed fwf. 

## Analysis
This contains different notebooks to analyse freshwater output from runs quickly. `analysis/plot_fwf_compare_2_exps.ipynb` compares 2 different runs. 
