# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:07:02 2021

@author: Pc
"""

#prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import numpy as np
N=600851475143
def max_prime_fact(N):
    
    f=[]
    
    for number in range(N):
        if N%(number+1)==0:
            f=f+[number+1]

    factor=np.array(f)

    for l in range(len(f)):
        if all(factor[l]%factor[1:l])!=0:
            PF=factor[l];
    return PF