# --------------------------------------------------
# Adyacency matrix construction for Network based on
# Information Transference for Colombia
# -------------- -----------------------------------

# libraries

import numpy as np
import xarray as xr
import pandas as pd


def get_data_per_index(index_name):
    """
    Import tp, t2m and vimflux nc files for a given index
    Input: index_name - str
    """

    # total precipitation
    DS = xr.open_dataset("col-inf-transf-data/T_" + index_name + "_tp.nc")
    ds_tp = DS.to_dataframe()

    # two meter temperature
    DS = xr.open_dataset("col-inf-transf-data/T_" + index_name + "_t2m.nc")
    ds_t2m = DS.to_dataframe()

    # vertical integral of moisture flux
    DS = xr.open_dataset("col-inf-transf-data/T_" + index_name + "_vimflux.nc")
    ds_vimflux = DS.to_dataframe()

    return ds_tp, ds_t2m, ds_vimflux


def filter_flux_around_zero(df, threshold = 0.5/100):
    """
    Set to zero absolute information flux below threshold
    Input:  df - DataFrame, threshold - float
    """

    df[df.columns[0]] = df.tau21.apply(lambda x: 0.0 if np.abs(x) < threshold else x)

    return True

def build_adjacency_matrix(df, threshold = 0.5/100):

    adj_matrix = np.zeros((len(df), len(df)))

    for i in np.arange(len(df)):
        if df.tau21[i] != 0.0:
            adj_matrix[i] = ((df.tau21 > df.tau21[i]-threshold) & (df.tau21 < df.tau21[i]+threshold)).astype(int).values

    return adj_matrix

def my_network_adjacency_matrix(index):
    """
    Returns adjacency matrix for one index using tp, t2m and vimflux information flux
    Input: index - str
    """

    # threshold for minimum normalized information transference 0.5%
    msc_threshold = 0.5/100

    # get index data
    df_tp, df_t2m, df_vimflux = get_data_per_index(index)

    # take out low flux values
    filter_flux_around_zero(df_tp, msc_threshold)
    filter_flux_around_zero(df_t2m, msc_threshold)
    filter_flux_around_zero(df_vimflux, msc_threshold)

    # build adyacency matrix per index
    adj_tp = build_adjacency_matrix(df_tp, msc_threshold)
    adj_t2m = build_adjacency_matrix(df_t2m, msc_threshold)
    adj_vimflux = build_adjacency_matrix(df_vimflux, msc_threshold)

    # whole network adyacency matrix
    my_net_adj_matrix = adj_tp + adj_t2m + adj_vimflux
    my_net_adj_matrix[my_net_adj_matrix != 0] = 1  # no weighted conection

    return my_net_adj_matrix


car_network = my_network_adjacency_matrix("car")
np.savetxt('tau-networks-by-index/car_adj_matrix.txt', car_network, fmt='%i')

nino3_network = my_network_adjacency_matrix("nino3")
np.savetxt('tau-networks-by-index/nino3_adj_matrix.txt', nino3_network, fmt='%i')

nino34_network = my_network_adjacency_matrix("nino34")
np.savetxt('tau-networks-by-index/nino34_adj_matrix.txt', nino34_network, fmt='%i')

nta_network = my_network_adjacency_matrix("nta")
np.savetxt('tau-networks-by-index/nta_adj_matrix.txt', nta_network, fmt='%i')

soi_network = my_network_adjacency_matrix("soi")
np.savetxt('tau-networks-by-index/soi_adj_matrix.txt', soi_network, fmt='%i')

tna_network = my_network_adjacency_matrix("tna")
np.savetxt('tau-networks-by-index/tna_adj_matrix.txt', tna_network, fmt='%i')
