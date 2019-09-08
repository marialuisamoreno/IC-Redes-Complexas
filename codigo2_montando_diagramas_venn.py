from collections import defaultdict 
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy
import sys

# Inserindo valores
arq1 = "HS68.txt"
arq2 = "HS895T.txt"
print ("Lendo dados...")
print ("Inserindo informações...")

dados1 = [] 
dados2 = []

with open(arq1, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()

        dados1.append(dado)
dados.close()

with open(arq2, "r") as dados:
    for linha in dados:
        linha = linha.replace("\n", "") # tirando o \n do final
        linha = linha.replace(" ", " ") # tirando o tab

        dado, valor = linha.split()

        dados2.append(dado)
dados.close()

v = venn2(subsets=(set(dados1), set(dados2)), set_labels=("HS68", "HS895T"), set_colors=("b", "g"))
plt.savefig("Diagrama_HS68_HS895T.png", format="PNG")
# plt.show()

A = set(dados1)
B = set(dados2)

intersecao = A.intersection(B)
# print(intersecao)
file = open("intersecao.txt","w") 
for i in intersecao:
    file.write(i +  "\n")
file.close()

# Elementos que não pertencem a interseção
file = open("regiao_HS68.txt","w") 
cont = 0
for i in dados1:
    if i in intersecao: cont += 1
    else: file.write(i +  "\n")
file.close()

file = open("regiao_HS895T.txt","w") 
cont = 0
for i in dados2:
    if i in intersecao: cont += 1
    else: file.write(i +  "\n")
file.close()
