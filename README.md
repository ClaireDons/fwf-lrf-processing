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


## 3. Changes to EC-Earth

## NEMO files (compile nemo after these changes)
path: sources/nemo-3.6/CONFIG/ORCA1L75_LIM3/MY_SRC/
- sbc_oce.F90
- sbccpl.F90
- sbcfwf.F90
- sbcmod.F90
- sbcrnf.F90

## EC-Earth scripts
path: runtimes/classic/

- ece-esm.sh.tmpl
- config-run.xml
- wrapper-hpc2020.sh
- fwfwrapper.sh                 - calls python scripts from ece-esm.sh.tmpl             -
- /ctrl/namelist.nemo-ORCA1L75-coupled.cfg.sh 

### Input files
path: fwf/interactive/input

- areacello_Ofx_EC-Earth3_historical_r1i1p1f1_gn.nc
- basal_melt_mask_ORCA1_ocean.nc
- calving_mask_ORCA1_ocean.nc
- basal_melt_depth1.nc - created by InitialiseFreshwaterForcing.py 
- basal_melt_depth2.nc - created by InitialiseFreshwaterForcing.py
- FWF_LRF_y1850.nc - created by InitialiseFreshwaterForcing.py
- OceanSectorThetao_piControl.csv - mean ocean temperatures at depth of ice shelf base for piControl period

Note: after running InitialiseFreshwaterForcing.py 3 input files are created, you can also copy them from the input directory to the directory fwf/interactive/forcing_files/{exp}

path: fwf/
- runoff_maps_fwf_AIS.nc    - new file for runoff-mapper, excludes Antarctica

### Monitoring/output files
path: fwf/interactive/forcing_files

Output
- FWF_LRF_y????.nc - annual freshwater forcing file (basal melt + calving) to be read in by nemo

Monitoring
- OceanSectorThetao_{exp}_{year_min}_{year_max}.csv
- OceanSectorThetao_30yRM_{exp}_{year_min}_{year_max}.csv - 30 yr running mean
- BasalMeltAnomaly_{exp}_{year_min}_{year_max}.csv
- CumulativeFreshwaterForcingAnomaly_{exp}_{year_min}_{year_max}.csv
- TotalFreshwaterForcing_{exp}_{year_min}_{year_max}.csv - sum of anomalies + baseline
