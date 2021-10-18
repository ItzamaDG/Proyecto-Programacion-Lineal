# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:25:02 2021

@author: itzam
"""
import numpy as np
def generalKleeMinty(m):
    c = np.ones(m).reshape(m,1)
    A = np.zeros((m,m))
    b = np.zeros((m,1))
    
    
    for i in range(m):
        for j in range(i):
            A[i,j]=2
        b[i][0]= np.power(2,i+1)-1
        A[i,i]=1
        
    
    return (A,b,c)
    