# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:14:28 2021

@author: Pc
""
#problem 1

 s=[];
for n in range(1,1000):
    if n%3==0 or n%5==0:
        s=s+[n]
print(sum(s))