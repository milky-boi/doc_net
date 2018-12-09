import collections 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

mreza = nx.read_weighted_edgelist("tez_edg.edges" , delimiter = ' ' )
G=nx.Graph(mreza)
nx.draw(G)
plt.show()

cvorovi = np.float64(G.number_of_nodes())
veze = np.float64(G.number_of_edges())

deg = [val for (node, val) in G.degree(weight='weight')]

cnt = []
for i in range (30):
    cnt.append(i)

fig, ax = plt.subplots()
plt.bar(cnt, deg, color='b')

plt.title("Degree Histogram")
plt.ylabel("Degree")
plt.xlabel("Nodes")
#plt.xticks(deg, fontsize=9, rotation=45)
#ax.set_xticks([d + 0.4 for d in deg])
#ax.set_xticklabels(deg)
plt.savefig('degree_histogram.png', dpi=200)


plt.show()
