#!/bin/bash
module load cdo

#name of grid description file
outgrid='/home/nk0j/preprocessing/ncfiles/zshelf_200m.nc'

#names of input and output model data files
infile='/home/nk0j/preprocessing/ncfiles/calving_mask.nc'
outfile='/home/nk0j/preprocessing/ncfiles/calving_mask_ORCA1.nc'

# Excute the regridding
cdo remapbil,$outgrid $infile $outfile

