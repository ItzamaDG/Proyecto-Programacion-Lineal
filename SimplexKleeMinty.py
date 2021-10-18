# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:21:18 2021

@author: itzam
"""
from generalKleeMinty import generalKleeMinty
from mSimplexFaseII import mSimplexFaseII
import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt

iteraciones = np.zeros(8,dtype=int)
tiempos = np.zeros(8)
for k in range(3,11):
    A,b,c = generalKleeMinty(k)
    start = timer()
    x,z_0,estatus,itera = mSimplexFaseII(A,b,c)
    end = timer()
    tiempos[k-3]=end-start
    iteraciones[k-3] = itera
    
plt.plot(np.arange(3,11),tiempos)
    

    
    