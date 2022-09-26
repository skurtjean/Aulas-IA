# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:26:44 2022

@author: lab56
"""

from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot
import matplotlib
import matplotlib.pyplot as plt

def degrau(x):
    return 1 if x >= 0 else 0

def saida_perceptron(pesos, entradas):
    y = dot(pesos, entradas)
    return degrau(y)

def ajustes(sinapses, entradas, saida):
    
    taxa_aprendizagem = 0.08
    
    saida_parcial = saida_perceptron(sinapses, entradas)
    
    for j in range(3):
        sinapses[j] = sinapses[j] + taxa_aprendizagem * (saida[0] - saida_parcial) * entradas[j]
        
    saida = saida_parcial
    return sinapses, saida

def teste_generalização(sinapses, entradas, saida):
    saida_parcial = saida_perceptron(sinapses, entradas)
    saida = saida_parcial
    return sinapses, saida

neuronio = [0.22, -0.33, 0.44]
padrao_0_0 = [-1, 0.1, 0.1]
padrao_0_1 = [-1, 0.1, 0.5]
padrao_0_2 = [-1, 0.3, 0.3]
padrao_1_0 = [-1, 0.6, 0.6]
padrao_1_1 = [-1, 0.8, 0.2]
padrao_1_2 = [-1, 0.9, 0.5]

saida0 = [0]
saida1 = [1]
 # 11 ciclos de treinamento
n = 0;
for _ in range(11):
    neuronio, saida_0 = ajustes(neuronio, padrao_0_0, saida0)
    print (neuronio,"saida0 =", saida_0)
    neuronio, saida_0 = ajustes(neuronio, padrao_0_1, saida0)
    print (neuronio,"saida0 =", saida_0)
    neuronio, saida_0 = ajustes(neuronio, padrao_0_2, saida0)
    print (neuronio,"saida0 =", saida_0)
    neuronio, saida_1 = ajustes(neuronio, padrao_1_0, saida1)
    print (neuronio,"saida1 =", saida_1)
    neuronio, saida_1 = ajustes(neuronio, padrao_1_1, saida1)
    print (neuronio,"saida1 =", saida_1)
    neuronio, saida_1 = ajustes(neuronio, padrao_1_2, saida1)
    print (neuronio,"saida1 =", saida_1)
    n = n + 1;
    print ("número de ciclos = ", n)
    

x = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
y = [-0.125, -0.0125, 0.1, 0.2125, 0.325, 0.4375, 0.55, 0.6625, 0.775, 0.8875]
# y = 1.0 - 1.125*x - equação de reta de separação de classes
x1 = [0.1, 0.1, 0.3]
x2 = [0.6, 0.8, 0.9]
y1 = [0.1, 0.5, 0.3]
y2 = [0.6, 0.2, 0.5]
#insere os pontos x1, y1, x2, y2 no gráfico
plt.scatter(x1, y1)
plt.scatter(x2, y2)

plt.plot(y, x, color = 'green', marker = '*', linestyle = '--')
#definição dos nomes das opções linestyle
"""
a valid value for ls; supported values are '-',
'--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
 """
plt.title("separação de classes com Perceptron")
 
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.show()




#teste de generalização
padrao_teste_0 = [-1, 0.2, 0.4]
padrao_teste_1 = [-1, 0.7, 0.8]
padrao_teste_2 = [-1, 0.6, 0.3]
padrao_teste_3 = [-1, 0.1, 0.9]
padrao_teste_4 = [-1, 0.2, 0.6]
padrao_teste_5 = [-1, 0.8, 0.1]
#teste de generalização
print("teste de generalização")
neuronio, saida_0 = teste_generalização(neuronio, padrao_teste_0, saida0)
print (neuronio,"saida0 =", saida_0)
neuronio, saida_1 = teste_generalização(neuronio, padrao_teste_1, saida1)
print (neuronio,"saida1 =", saida_1)
neuronio, saida_0 = teste_generalização(neuronio, padrao_teste_2, saida0)
print (neuronio,"saida0 =", saida_0)
neuronio, saida_1 = teste_generalização(neuronio, padrao_teste_3, saida1)
print (neuronio,"saida1 =", saida_1)
neuronio, saida_0 = teste_generalização(neuronio, padrao_teste_4, saida0)
print (neuronio,"saida0 =", saida_0)
neuronio, saida_1 = teste_generalização(neuronio, padrao_teste_5, saida1)
print (neuronio,"saida1 =", saida_1)