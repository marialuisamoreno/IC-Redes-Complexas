from collections import defaultdict 
import matplotlib.pyplot as plt
import sys

value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
 
box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data)
plt.show()

# Arquivos com os dados
arq_lqf = []
arq_lqf.append("A375.txt")
arq_lqf.append("HS68.txt")
arq_lqf.append("HS895SK.txt")
arq_lqf.append("HS895T.txt")
arq_lqf.append("SH4.txt")
lqf = {}
arq_betweenness = "betweenness.txt"
bet = {}
arq_closeness = "closeness.txt"
clo = {}
arq_clustering = "clustering.txt"
clu = {}
arq_currentflowbetweenness = "currentflowbetweenness.txt"
cfb = {}
arq_currentflowcloseness = "currentflowcloseness.txt"
cfc = {}
arq_degree = "degree.txt"
deg = {}
arq_eccentricity = "eccentricity.txt"
ecc = {}
arq_eigenvector = "eigenvector.txt"
eig = {}
arq_harmonic = "harmonic.txt"
har = {}
arq_load = "load.txt"
loa = {}
arq_pagerank = "pagerank.txt"
pag = {}
arq_subgraph = "subgraph.txt"
sub = {}

for arq in arq_lqf:
    print (arq)
    # lqf
    aux = 0
    i = 0
    with open(arq, "r") as dados:
        for linha in dados:
            linha = linha.replace("\n", "") # tirando o \n do final
            linha = linha.replace(" ", " ") # tirando o tab

            dado, valor = linha.split()
            valor = valor.replace(",", ".") # colocando para EN
            lqf[i]["lqf_" + aux] = valor
            i += 1
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
