# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:42:02 2018

@author: mile
"""
import networkx as nx 
import re 
import collections 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from collections import Counter

G=nx.MultiGraph()

veze = []
svi_nodesi = []

for i in range(30):
    
    s = open("nodes/all_nodes_s %s.txt" %i, "r")
    s = s.read()
    s = re.findall(r'\b[a-z]{2,25}\b', s)
    
    svi_nodesi.append(s)
    
file = open("veze/veze.edges" , "w")

for broj_noda in range (len(svi_nodesi)):
    doc_nodes = (svi_nodesi[broj_noda])
    od =broj_noda+1
    
    for broj in range(od, len(svi_nodesi)):
        
        if (broj_noda != broj):
            drugi_node = str(svi_nodesi[broj])
            for i in range(50):
                vrijednost_prvog = str(doc_nodes[i]) 
                if (vrijednost_prvog in drugi_node ):
                    prvi_cvor = str(broj_noda)
                    drugi_cvor = str(broj)
                    rijec = vrijednost_prvog
                    file.write(prvi_cvor)
                    file.write(" ")
                    file.write(drugi_cvor)
                    file.write(" ")
                    #file.write(rijec)
                    file.write("\n")
                        
file.close()

file = open("veze/veze.edges", "r")
file = file.read()
file = file.split("\n")

broj = Counter(file)
cvorovi = list(broj.keys())
tezina = list(broj.values())

edges = []

for i in range (len(cvorovi)):
    edges.append(str(cvorovi[i]) + str(tezina[i]))

file = open("tez_edg.edges", "w")

for i in range(len(edges)):
    file.write(edges[i])
    file.write("\n")
    
file.close()

mreza = nx.read_weighted_edgelist("tez_edg.edges" , delimiter = ' ' )
G=nx.Graph(mreza)
nx.draw(G)
plt.show()
plt.savefig('graf.png', dpi=200)


deg = [val for (node, val) in G.degree(weight='weight')]
deg = sorted(deg, reverse = True)
cnt = []
for i in range (30):
    cnt.append(i)

fig, ax = plt.subplots()
plt.bar(cnt, deg, color='b')
plt.title("Degree Histogram")
plt.ylabel("Degree")
plt.xlabel("Nodes")
plt.savefig('degree_histogram.png', dpi=200)
plt.show()        
        
file.close()

cvorovi = np.float64(G.number_of_nodes())
veze = sum(deg)
prosjecni_stupanj = (2*veze)/cvorovi
gustoca_mreze = nx.density(G)

duljine_puta = []
for C in nx.connected_component_subgraphs(G):
    duljina = nx.average_shortest_path_length(C)
    duljine_puta.append(duljina)

sortirani = sorted(duljine_puta, reverse = True)
dijametri = []
for C in nx.connected_component_subgraphs(G):
    duljina = nx.diameter(C)
    dijametri.append(duljina)

sortirani_dijametri = sorted(dijametri, reverse = True)

file=open('graph_glob_stats.txt','w')
file.write('Broj cvorova: ' + str(cvorovi) + '\n')
file.write('Broj veza: '+ str(veze) + '\n' )
file.write('Prosjecan stupanj: ' + str(prosjecni_stupanj) + '\n')
file.write('Gustoca mreze: ' + str(gustoca_mreze) + '\n')
file.write('Prosjecna duljina najkraceg puta: ' + str(sortirani[0]) + '\n' )
file.write('Dijametar mreze: ' + str(sortirani_dijametri[0]) + '\n')

file.close()







