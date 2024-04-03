#¡/bin/bash

# --------------------------------------------------------
# Runs tau 2-1 calculation for all datasets
# --------------------------------------------------------
# origin path variables: variables-data/era5-data/
# origin path indexes: indexes-data/anomalies-glob/

# initialize variables and indexes folders

idxorigin="indexes-data/anomalies-glob"
varorigin="variables-data/era5-data"

# Get files directory and files name as options
while [ ! -z "$1" ]; do
  case "$1" in
     --variablesfolder|-fvar)
         shift
         varorigin=$1
         ;;
     --indexesfolder|-fidx)
         shift
         idxorigin=$1
         ;;
     *)
        Help
        exit
        ;;
  esac
shift
done

# ---------------------------------
# Main program
# ---------------------------------

for idxfile in $idxorigin/*.nc

do
    for varfile in $varorigin/*.nc

        do
            # extract variable and index name from folder name
            var=${varfile%.*}
            var=${var##*/}
            idx=${idxfile%_*}
            idx=${idx##*/}

            echo $var and $idx runs $varfile and $idxfile

            # run bash script

            bash inf_transf_calculation.sh -fvar $varfile -findex $idxfile -varname $var -idxname $idx
        done

done