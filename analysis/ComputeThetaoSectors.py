# Compute Antarctic freshwater forcing anomalies from ocean subsurface temperature in 5 regions
# 2023-03: Eveline van der Linden (KNMI) linden@knmi.nl

## Import modules
import os
import xarray as xr
import pandas as pd
import numpy as np
import sys

import ThetaoSectors as TS

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

## Year of run + total experiment
#year = int(sys.argv[3])
year_min = int(sys.argv[1])
year_max = int(sys.argv[2])
leg = int(sys.argv[3])
leg_number = str(sys.argv[3]).zfill(3) # add leading zeros
exp_name = str(sys.argv[4])
start_dir = str(sys.argv[5])
run_dir = str(sys.argv[6])

year = year_min + leg - 1
print('year: ', year)

########################## File definition #########################
## Paths
path_input = f'{start_dir}/fwf/interactive/input/'
path_output = f'{start_dir}/fwf/interactive/forcing_files/{exp_name}/'

## Input data
## Output file from nemo: input file for freshwater forcing
file_thetao = f'{run_dir}/output/nemo/{leg_number}/{exp_name}_1m_{year}0101_{year}1231_opa_grid_T_3D.nc' #other output format
file_area = f'{path_input}/areacello_Ofx_EC-Earth3_historical_r1i1p1f1_gn.nc'

## Output data
output_thetao =f'{path_output}/OceanSectorThetao_{exp_name}_{year_min}_{year_max}.csv'

##################### Sector mean thetao computation ############################

## Open thetao dataset + rename dimensions (to be consistent with areacello file)
ds = xr.open_dataset(file_thetao)
ds = ds.rename({'y':'j','x':'i','nav_lon':'longitude','nav_lat':'latitude','olevel':'lev'})

## Compute time mean value over annual file 
ds_thetao_year = ds['thetao'].mean('time_counter')

# Read lev bnds
ds_lev_bnds = ds['olevel_bounds']

## Open areacello dataset
ds_area = xr.open_dataset(file_area)

## Sector names, consistent with linear response functions
sectors = ['eais','wedd','amun','ross','apen']

## Create dataframe for mean ocean temperatures per sector
df_thetao_year = pd.DataFrame(columns=sectors, index=[year])
df_thetao_year.index.name = 'year'

## Loop over oceanic sectors
for sector in sectors:

    # Compute area weighted mean temperature
    print('Computing area weighted mean of thetao for ', sector, 'sector')           
    thetao_area_weighted_mean = TS.area_weighted_mean(ds_thetao_year,ds_area,sector)

    # Compute layer weighted mean of area weighted mean --> volume weighted mean
    thetao_volume_weighted_mean = TS.lev_weighted_mean(thetao_area_weighted_mean,ds_lev_bnds,sector)

    # Create dataframe from dataarray
    print('Fill dataframe for sector ', sector)
    df_thetao_year[sector] = [thetao_volume_weighted_mean.values]

## Export data 
print(f'##### Exporting data of year {year} to csv file ##############')
print(output_thetao)

if year==year_min:
    # Create output file for the first year
    if os.path.isfile(output_thetao):    
        os.remove(output_thetao)    

    df_thetao_year.to_csv(output_thetao)
elif year>year_min:
    # Append to existing file (if file exists)
    df_thetao_year.to_csv(output_thetao, mode='a', header=not os.path.exists(output_thetao))

ds_area.close()

