from collections import defaultdict 
import matplotlib.pyplot as plt
import community
import networkx as nx
import numpy
import sys

G = nx.Graph()

# Inserindo valores
arq = []
arq.append("A375.txt")
arq.append("HS68.txt")
arq.append("HS895SK.txt")
arq.append("HS895T.txt")
arq.append("SH4.txt")

proteina = arq[4]   # trocar aqui para cada rede!

print ("Lendo dados...")
print ("Inserindo informações...")
with open(proteina, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        vertice, value = linha.split()
        value = value.replace(",", ".") # trocando para EN

        G.add_node(vertice, dado = float(value))      
dados.close()

print ("Abrindo arquivo com as arestas")
arq_arestas = "1_arestas_filtradas.txt"
print ("Lendo dados...")
print ("Inserindo vértices e arestas...")

# Lendo as arestas
with open(arq_arestas, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        # todas as informações são lidas aqui
        vertice1, vertice2 = linha.split()

        if vertice1 in G.nodes() and vertice2 in G.nodes():
            if 'dado' in G.node[vertice1] and 'dado' in G.node[vertice2]:
                peso = (float(G.node[vertice1]['dado']) + float(G.node[vertice2]['dado']))/2
                G.add_edge(vertice1, vertice2, weight = peso)   
dados.close()
print ("Arestas registradas com sucesso!")
print ("")

totalVert0 = G.number_of_nodes()  # total de proteinas inseridas
# GRAU ---------------------------------------------------------------------------------------------------------------------
print ("Calculando o grau dos vétices...")
file = open("degree.txt","w") 
i = 0
removidos = 0
nodes = list(G.nodes())
degree = [val for (node, val) in G.degree()]
while i < totalVert0:
    if degree[i] == 0:          # se é um nó sozinho, removo do grafo
        G.remove_node(nodes[i])
        removidos += 1
   
    else: file.write(str(nodes[i]) + "    " + str(degree[i]) + "\n")
    i = i+1
file.close()

totalVert = G.number_of_nodes()    # total de proteinas pertencentes a rede
totalArestas = G.number_of_edges() # total de arestas da rede

# CLOSENESS ----------------------------------------------------------------------------------------------------------------
print ("Calculando closeness...")
grafo = G.nodes()
file = open("closeness.txt","w") 
closeness = nx.closeness_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(closeness[vert]) + "\n")
file.close()

# BETWEENNESS --------------------------------------------------------------------------------------------------------------
print ("Calculando betweenness...")
file = open("betweenness.txt","w") 
betweenness = nx.betweenness_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(betweenness[vert]) + "\n")
file.close()

# CLUSTERING ---------------------------------------------------------------------------------------------------------------
print ("Calculando clustering...")
file = open("clustering.txt","w") 
clustering = nx.clustering(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(clustering[vert]) + "\n")
file.close()

# EIGENVECTOR --------------------------------------------------------------------------------------------------------------
print ("Calculando eignvecto...")
file = open("eigenvector.txt","w") 
eigenvector = nx.eigenvector_centrality_numpy(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(eigenvector[vert]) + "\n")
file.close()

# CURRENT FLOW CLOSENESS ---------------------------------------------------------------------------------------------------
print ("Calculando current flow closeness...")
file = open("currentflowcloseness.txt","w") 
currentflowcloseness = nx.current_flow_closeness_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(currentflowcloseness[vert]) + "\n")
file.close()

# CURRENT FLOW BETWEENNESS -------------------------------------------------------------------------------------------------
print ("Calculando current flow betweenness...")
file = open("currentflowbetweenness.txt","w") 
currentflowbetweenness = nx.current_flow_betweenness_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(currentflowbetweenness[vert]) + "\n")
file.close()

# LOAD ---------------------------------------------------------------------------------------------------------------------
print ("Calculando load...")
file = open("load.txt","w") 
load = nx.load_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(load[vert]) + "\n")
file.close()

# SUBGRAPH -----------------------------------------------------------------------------------------------------------------
print ("Calculando subgraph...")
file = open("subgraph.txt","w") 
subgraph = nx.subgraph_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(subgraph[vert]) + "\n")
file.close()

# HARMONIC -----------------------------------------------------------------------------------------------------------------
print ("Calculando harmonic...")
file = open("harmonic.txt","w") 
harmonic = nx.harmonic_centrality(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(harmonic[vert]) + "\n")
file.close()

# PAGERANK -----------------------------------------------------------------------------------------------------------------
print ("Calculando pagerank...")
file = open("pagerank.txt","w") 
pagerank = nx.pagerank(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(pagerank[vert]) + "\n")
file.close()

# ECCENTRICITY -------------------------------------------------------------------------------------------------------------
print ("Calculando eccentricity...")
file = open("eccentricity.txt","w") 
eccentricity = nx.eccentricity(G)
for vert in grafo:
    file.write(str(vert) + '    ' + str(eccentricity[vert]) + "\n")
file.close()

# DADOS GERAIS -------------------------------------------------------------------------------------------------------------
print ("Salvando informações...")
file = open("0_infos.txt","w") 
file.write("Nome do arquivo: " + proteina + "\n")
file.write("Proteinas inseridas: " + str(totalVert0) + "\n")
file.write("Proteinas removidas: " + str(removidos) + "\n")
file.write("Proteinas com conexões: " + str(totalVert) + "\n")
file.write("Total de ligações: " + str(totalArestas) + "\n")
file.close()