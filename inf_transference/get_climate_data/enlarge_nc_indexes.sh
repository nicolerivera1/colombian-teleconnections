#¡/bin/bash

# -----------------------------------------------
# Enlarge all ncfiles in folder to a global grid
# -----------------------------------------------

# gets files directory and files name
read -p "origin folder: " origin
read -p "destination folder: " destin

for file in $origin/*.nc

do
    # to change grid size and fill extras with values from last grid
    cdo enlarge,grid_global -selyear,1951/2019 $file "$destin/${file:20}"
done
