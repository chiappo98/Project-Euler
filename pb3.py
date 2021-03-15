# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:07:02 2021

@author: Pc
"""

#prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import numpy as np

def max_prime_fact(N):
    
    d=[]
    
    for number in range(N):     #create an array of divisors of N
        if N%(number+1)==0:
            d=d+[number+1]

    div=np.array(d)

    for l in range(len(d)):         #only the prime factors are selected 
        if all(div[l]%div[1:l])!=0:
            PF=div[l];
    return PF

N=600851475143
rad=int(np.sqrt(N))

while N%rad!=0:                 #factorization of N into 2 smaller numbers
    rad=rad+1

f1=rad
f2=int(N/rad)

pf1=max_prime_fact(f1)          #calculate the max prime factor of each number
pf2=max_prime_fact(f2)

if pf2%pf1==0:
    maxPF=pf1
else maxPF=max(pf1,pf2)

print(maxPF)