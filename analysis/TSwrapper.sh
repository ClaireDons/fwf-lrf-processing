# Compute mean temperature for each of the 5 levermann regions
# Loop over the years
# Calls ComputeThetaoSectors.py each year
module load python3

run_start_date=2015
run_end_date=2100
#leg_start_date_yyyy=2015
#leg_number=1
exp_name=B852
start_dir=/perm/nk0j/ecearth3-cmip6/runtime/classic
run_dir=/ec/res4/scratch/nlcd/r9469-cmip6-bisi-knmi/B852

echo $run_start_date
echo $run_end_date
#echo $leg_start_date_yyyy
echo $exp_name
echo $start_dir
echo $run_dir

#!/bin/bash
for leg_number in {1..84}
do
    echo $leg_number
    #python3 ${start_dir}/fwf/interactive/scripts/ComputeThetaoSectors.py ${run_start_date} ${run_end_date} ${leg_start_date_yyyy} ${leg_number} ${exp_name} ${start_dir} ${run_dir}
    python3 ComputeThetaoSectors.py ${run_start_date} ${run_end_date} ${leg_number} ${exp_name} ${start_dir} ${run_dir}
done


echo "Computed thetao per sector for year $((${leg_number}+${run_start_date}-1))"