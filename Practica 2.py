#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pylab import figure
import pylab
import networkx as nx
G=nx.read_weighted_edgelist('soda.txt', create_using=nx.Graph())
nx.draw(G, with_labels = True, node_size = [G.degree(i) * 100 for i in G.nodes()])
diam= nx.diameter(G)
node_degree = nx.degree(G)
vString = str(node_degree)
resultados = [node_degree, diam]
f=open("resultados.txt","w")
f.write(vString)
f.close()
pylab.show()