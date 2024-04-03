#¡/bin/bash

# --------------------------------------------------------
# Selects spatial box that includes Colombia
# --------------------------------------------------------
#
# longitud 5S - 15 N and latitude 90W - 60W

# initialize variables and indexes folders

origin="tau-norm-glob"
destin="tau-norm-col"

# Get files directory and files name as options
while [ ! -z "$1" ]; do
  case "$1" in
     --originfolder|-forigin)
         shift
         origin=$1
         ;;
     --destinationfolder|-fdestin)
         shift
         destin=$1
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

for file in $origin/*.nc

do
    # get file name
    name=${file##*/}

    # to change grid size and fill extras with values from last grid
    cdo sellonlatbox,-90,-60,15,-5 $file "$destin/$name"
done