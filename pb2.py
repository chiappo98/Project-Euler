# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:41:20 2021

@author: Pc
"""
n=[0,1]
y=[]
while n[-1]<4e6:
    n=n+[n[-1]+n[-2]]
    if (n[-1]+n[-2])%2==0:
        y=y+[n[-1]+n[-2]]
print(sum(y))