# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:39:28 2019

@author: asus
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

loc1 = pd.read_excel('Coordinates.xlsx')
Coordinates = np.array(loc1)
xx = Coordinates[:,0]
yy = Coordinates[:,1]
loc2 = pd.read_excel('distancematrix.xls')
distancematrix = np.array(loc2)

points=xx,yy
myarray=np.asarray(points)

n=myarray.shape[1]
l=list(range(1,n))
np.random.shuffle(l)
l.insert(0,6)
randompath=np.append(l,l[0])

print(randompath)

xrandompath = [xx[i] for i in [xx-1 for xx in randompath]]
yrandompath = [yy[i] for i in [yy-1 for yy in randompath]]
   
totallength = 0
for i in range(len(randompath)-1):
    totallength += distancematrix[randompath[i+1],1+randompath[i]]
    
print('Length of the random route: ',totallength)
plt.plot(xx,yy,'.',label = 'Cities')
plt.plot(xrandompath,yrandompath,label = 'Random Route')
plt.legend()

