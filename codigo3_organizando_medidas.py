from collections import defaultdict 
import sys

# Arquivos com os dados
arq_lqf = "SH4.txt"
arq_betweenness = "betweenness.txt"
arq_closeness = "closeness.txt"
arq_clustering = "clustering.txt"
arq_currentflowbetweenness = "currentflowbetweenness.txt"
arq_currentflowcloseness = "currentflowcloseness.txt"
arq_degree = "degree.txt"
arq_eccentricity = "eccentricity.txt"
arq_eigenvector = "eigenvector.txt"
arq_harmonic = "harmonic.txt"
arq_load = "load.txt"
arq_pagerank = "pagerank.txt"
arq_subgraph = "subgraph.txt"

# Dicionário para os dados
rede = {}
prot = []

# lqf
with open(arq_lqf, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        prot.append(dado)
        rede[dado] = {}
        rede[dado]["lqf"] = valor
dados.close()

# betweenness
with open(arq_betweenness, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["bet"] = valor
dados.close()

# closeness
with open(arq_closeness, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["closeness"] = valor
dados.close()

# clustering
with open(arq_clustering, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["clustering"] = valor
dados.close()

# currentflowbetweenness
with open(arq_currentflowbetweenness, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["currentflowbetweenness"] = valor
dados.close()

# currentflowcloseness
with open(arq_currentflowcloseness, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["currentflowcloseness"] = valor
dados.close()

# degree
with open(arq_degree, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["degree"] = valor
dados.close()

# eccentricity
with open(arq_eccentricity, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["eccentricity"] = valor
dados.close()

# eigenvector
with open(arq_eigenvector, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["eigenvector"] = valor
dados.close()

# harmonic
with open(arq_harmonic, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["harmonic"] = valor
dados.close()

# load
with open(arq_load, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["load"] = valor
dados.close()

# pagerank
with open(arq_pagerank, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["pagerank"] = valor
dados.close()

# subgraph
with open(arq_subgraph, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()
        valor = valor.replace(".", ",") # colocando para PT

        rede[dado]["subgraph"] = valor
dados.close()

# print(rede)

file = open("medidas_por_proteina.txt","w") 
file.write("proteina" + " " + "LQF" + " " + "Betweenness" + " " + "Closeness" + " " + "Clustering" + " " + "Currentflowbetweenness" + " " + "Currentflowcloseness" + " " + "Degree" + " " + "Eccentricity" + " " + "Eigenvector" + " " + "Harmonic" + " " + "Load" + " " + "Pagerank" + " " + "Subgraph" + "\n")

for i in prot:
    if ("bet" in rede[i]) == False: rede[i]["bet"] = '0'
    if ("closeness" in rede[i]) == False: rede[i]["closeness"] = '0'
    if ("clustering" in rede[i]) == False: rede[i]["clustering"] = '0'
    if ("currentflowbetweenness" in rede[i]) == False: rede[i]["currentflowbetweenness"] = '0'
    if ("currentflowcloseness" in rede[i]) == False: rede[i]["currentflowcloseness"] = '0'
    if ("degree" in rede[i]) == False: rede[i]["degree"] = '0'
    if ("eccentricity" in rede[i]) == False: rede[i]["eccentricity"] = '0'
    if ("eigenvector" in rede[i]) == False: rede[i]["eigenvector"] = '0'
    if ("harmonic" in rede[i]) == False: rede[i]["harmonic"] = '0'
    if ("load" in rede[i]) == False: rede[i]["load"] = '0'
    if ("pagerank" in rede[i]) == False: rede[i]["pagerank"] = '0'
    if ("subgraph" in rede[i]) == False: rede[i]["subgraph"] = '0'

    file.write(i + " " + rede[i]["lqf"] + " " + rede[i]["bet"] + " " + rede[i]["closeness"] + " " + rede[i]["clustering"] + " " + rede[i]["currentflowbetweenness"] + " " + rede[i]["currentflowcloseness"] + " " + rede[i]["degree"] + " " + rede[i]["eccentricity"] + " " + rede[i]["eigenvector"] + " " + rede[i]["harmonic"] + " " + rede[i]["load"] + " " + rede[i]["pagerank"] + " " + rede[i]["subgraph"] + "\n")
file.close()
