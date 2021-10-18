# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:25:02 2021

@author: itzam
"""
import numpy as np

def generalKleeMinty(m):
    c = np.ones(m).reshape(m,1)
    c *=-1
    A = np.tril(2*np.ones((m,m)),-1)+np.eye(m)
    b = np.power(2,np.arange(1,m+1))-1
    b = b.reshape(m,1)
    b = b.astype(dtype=float)
    
    return (A,b,c)
    