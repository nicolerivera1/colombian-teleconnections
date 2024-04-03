#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Title:: *)
(*Network Properties*)


(* ::Text:: *)
(*Automatic calculation and exportation of network properties for each index or a given adjacency matrix*)


(* ::Input::Initialization:: *)
data = Import["/home/nicole/adj-matrixes/nta_adj_matrix.txt","Table"];
gr = AdjacencyGraph[data, DirectedEdges->False, PlotTheme->"Monochrome" ];


(* ::Chapter:: *)
(*Graph Properties*)


cluster = {{"Global_Clustering_coef", GlobalClusteringCoefficient[gr]}, {"Mean_Clustering_coef", MeanClusteringCoefficient[gr]}};
Export["/home/nicole/wolf-properties/nta_clustering_coefs.csv", cluster, "CSV"]


(* ::Text:: *)
(*Properties that require an entire map*)


(* ::Input::Initialization:: *)
betcent = BetweennessCentrality[gr];
Export["/home/nicole/wolf-properties/nta_betweenness_centrality.csv", betcent, "CSV"];


(* ::Input::Initialization:: *)
localclust = LocalClusteringCoefficient[gr];
Export["/home/nicole/wolf-properties/nta_local_clustering.csv", localclust, "CSV"];
