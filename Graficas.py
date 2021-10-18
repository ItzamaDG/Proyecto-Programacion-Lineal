# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:44:45 2021

@author: itzam
"""

from mSimplexFaseII import mSimplexFaseII
import numpy as np
from matplotlib import pyplot as plt

# % generar dimensiones del problema
# m = round(10*exp(log(20)*rand()));
# n = round(10*exp(log(20)*rand()));
# % generar A, b, c
# sigma = 100;
# A = round(sigma*randn(m,n));
# b = round(sigma*abs(randn(m,1)));
# c = round(sigma*randn(n,1));

problemas = 50
n = np.round(10*np.exp(np.log(20)*np.random.uniform(size=problemas))).astype(dtype=int)
m = np.round(10*np.exp(np.log(20)*np.random.uniform(size = problemas))).astype(dtype = int)
#Aqui tenemos ya el tamaño del problema para cada problema
sigma = 100

iteraciones = np.zeros(problemas)
solucion_encontrada = np.zeros(problemas,dtype = int)

for i in range(problemas):

    A = np.round(sigma*np.random.normal(size = (m[i],n[i])))
    b = np.round(sigma*np.abs(np.random.normal(size=(m[i],1))))
    c = np.round(sigma*np.random.normal(size=(n[i],1)))
    x,z_0,estatus,itera = mSimplexFaseII(A,b,c)
    iteraciones[i]=itera
    solucion_encontrada[i] = estatus
    
    

minimo = np.minimum(m,n)
label = np.where(solucion_encontrada==0,"Solución Óptima","No Acotado")
colors = np.array(["#0F71BB","#BB260F"])
legend = np.array(["Solución Óptima","No Acotado"])
figure = plt.figure()
ax = plt.subplot(1,1,1)
ax.scatter(np.log10(minimo[label=="Solución Óptima"]),
            np.log10(iteraciones[label=="Solución Óptima"]),
            alpha=0.7,s=50,color = "#0F71BB")

ax.scatter(np.log10(minimo[label=="No Acotado"]),
            np.log10(iteraciones[label=="No Acotado"]),
            alpha=0.7,s=50,color = "#BB260F")


ax.set_xlabel("$\log(\min(m,n)$)")
ax.set_ylabel("$\log(Iteraciones)$")
ax.grid()
ax.legend(label)
    





# plt.scatter(minimo[label=="Solución Óptima"],
#             iteraciones[label=="Solución Óptima"],
#             alpha=0.7,s=50,color = "#0F71BB")

# plt.scatter(minimo[label=="No Acotado"],
#             iteraciones[label=="No Acotado"],
#             alpha=0.7,s=50,color = "#BB260F")



# fig, ax = plt.subplots(figsize=(8,8))

# for estado,color in zip(label,colors):
#     indices = np.where(label==estado)
#     ax.scatter(
#         minimo[indices], iteraciones[indices], label=estado,
#         s=50, color=color, alpha=0.7
#     )
