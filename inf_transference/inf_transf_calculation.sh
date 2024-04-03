#¡/bin/bash

# --------------------------------------------------------
# Computes normalization terms for the 
# Liang-Kleeman Information Transference T 2 -> 1 
# --------------------------------------------------------
#
# The formula used is the one with the correlations C_ij 
# described in Liang 2015

# OUTPUTS: one netcdf with tau and all the information transference terms


# ---------------------------------
# Help function
# ---------------------------------
Help()
{
   # Display Help
   echo "Calculation of the normalized Liang-Kleeman information transference"
   echo
   echo "Syntax: bash inf_transf_calculation.sh [h|V|g]"
   echo "options:"
   echo "g     Print the GPL license notification."
   echo "h     Print this Help."
   echo "v     Verbose mode."
   echo "V     Print software version and exit."
   echo
}

file1=" "
file2=" "
folder="tmp"
outfile="prueba.nc"
varname=" "
idxname="anommaly"

# ---------------------------------
# Main program
# ---------------------------------


# Get files directory and files name as options
while [ ! -z "$1" ]; do
  case "$1" in
     --variablefile|-fvar)
         shift
         file1=$1
         ;;
     --indexfile|-findex)
         shift
         file2=$1
         ;;
     --variablename|-varname)
         shift
         varname=$1
         ;;
     --indexname|-idxname)
         shift
         idxname=$1
         ;;
     --outputfile|-fout)
         shift
         outfile=$1
         ;;
     --temporalfolder|-tmp)
         shift
         folder=$1
         ;;
     *)
        Help
        exit
        ;;
  esac
shift
done


# calculating message
echo "Calculating normalization terms from $file2 to $file1"

# build output file name
outfile="T_${idxname}_${varname}.nc"

echo "for variable $varname and outputfile $outfile"


# ------ temporal files names ----- #
dvar1="$folder/d_var1_dt.nc"
dvar2="$folder/d_var2_dt.nc"
c11="$folder/cov_var1_var1.nc"
c22="$folder/cov_var2_var2.nc"
c12="$folder/cov_var1_var2.nc"
c1d1="$folder/cov_var1_dvar1.nc"
c2d1="$folder/cov_var2_dvar1.nc"
cd1d1="$folder/cov_dvar1_dvar1.nc"

# calculate varible 1 time derivative
cdo -b F64 mergetime -seltimestep,1 "$file1" -deltat "$file1" "$dvar1"

# calculate varible 2 time derivative
cdo -b F64 mergetime -seltimestep,1 "$file2" -deltat "$file2" "$dvar2"

# calculate time covariance between 1 and 2 
cdo -b F64 chname,"$varname","C12" -timcovar "$file1" "$file2" "$c12"

# calculate time covariance between 1 and 1 
cdo -b F64 chname,"$varname","C11" -timcovar "$file1" "$file1" "$c11"

# calculate time covariance between 2 and 2 
cdo -b F64 chname,"anommaly","C22" -timcovar "$file2" "$file2" "$c22"

# calculate time covariance between 1 and d1 
cdo -b F64 chname,"$varname","C1d1" -timcovar "$file1" "$dvar1" "$c1d1"

# calculate time covariance between d1 and d1 
cdo -b F64 chname,"$varname","Cd1d1" -timcovar "$dvar1" "$dvar1" "$cd1d1"

# calculate time covariance between 2 and d1 
cdo -b F64 chname,"anommaly","C2d1" -timcovar "$file2" "$dvar1" "$c2d1"

# merge all correlation files into one
cdo -b F64 merge "$c12" "$c11" "$c22" "$c1d1" "$cd1d1" "$c2d1" "$folder/merged_covars.nc"

# calculate all terms and tau
cdo -b F64 exprf,cdo_expr_for_tau_calculation.txt "$folder/merged_covars.nc" "tau-norm-glob/$outfile"

# erase all temporal files
rm $folder/*.nc

