# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:42:01 2021

@author: Pc
"""
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit 
#numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


#possible steps:
#       -among 6-digit numbers find those that are palindrome
#        (starting from 999999 and going back)
#       -the number must be the product of TWO 3-digit numbers

#a 3-digit number goes from 100 to 999

import numpy as np    
n=np.arange(10,100,1)

threeDig=n.reshape(len(n),1)@n.reshape(1, len(n))
tD=threeDig.reshape(len(threeDig)**2,1)

for i in range(len(tD)):
    cm=0#int(tD[i]/1e5)
    dm=0#int((tD[i]-cm*1e5)/1e4)
    m=int((tD[i]-(cm*1e5+dm*1e4))/1e3)
    c=int((tD[i]-(cm*1e5+dm*1e4+m*1e3))/1e2) 
    d=int((tD[i]-(cm*1e5+dm*1e4+m*1e3+c*100))/10)  
    u=int(tD[i]-(cm*1e5+dm*1e4+m*1e3+c*100+d*10))    
    
    #if ((cm==u)and(dm==d)and(m==c)):
    if ((m==u)and(c==d)):
        pal=tD[i]

print(pal)