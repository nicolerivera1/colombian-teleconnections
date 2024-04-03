# ---------------------------------------------------
# Calculates all Graph Properties for using NetworkX
# -------------- ------------------------------------

# libraries
import numpy as np
import networkx as nx
import pandas as pd
# import xarray as xr
# import matplotlib.pyplot as plt

def update_adj_matrix(index_name):
    print('Filling diagonal with zeros for :', index_name)
    path = "adj_matrixes/" + index_name + "_adj_matrix.txt"

    adj_matrix = np.loadtxt(path)
    np.fill_diagonal(adj_matrix, 0)

    np.savetxt(path, adj_matrix, fmt = "%d")
    
def get_graph(index_name):
    """
    Reads adjacency matrix in txt file and returns NetworkX graph
    """
    #print("Reading and creating graph for ", index_name)
    path = "adj-matrixes/" + index_name + "_adj_matrix.txt"

    G = nx.from_numpy_array(np.loadtxt(path))

    return G

def get_properties(Graph, index_name):
    """
    Calculates all network properties for a given graph
    and saves files with the results using index name
    """

    clust_dict = nx.clustering(Graph)
    pd.DataFrame(clust_dict.values(), index = clust_dict.keys()).to_csv('net-properties/' + index_name + '_clustering.csv', header = False)

    betweenness_dict = nx.betweenness_centrality(Graph)
    pd.DataFrame(betweenness_dict.values(), index = betweenness_dict.keys()).to_csv('net-properties/' + index_name + '_betweenness.csv', header = False)

    avg_clust = nx.average_clustering(Graph)
    np.savetxt('net-properties/'+ index_name +'_avg_clust.txt', np.array([avg_clust]))

    return True


if __name__ == "__main__":

    indexes = ["car", "nino3", "nino34", "nta", "tna", "soi"]

    for index in indexes:
        try:
            graph = get_graph(index)
            get_properties(graph, index)
        except Exception as e:
            print(e)