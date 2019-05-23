# -*- coding: utf-8 -*-
"""
Created on Thu May 23 01:42:39 2019

@author: asus
"""

import matplotlib.pyplot as plt
import xlrd
import numpy as np

loc = ("C:/Users/asus/Desktop/phyton_final/Coordinates.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
print('number of rows='+str(sheet.nrows))
print('number of columns='+str(sheet.ncols))

a=[]
for i in range(sheet.nrows-1):
    for n in range(sheet.ncols-2):
        a.append(sheet.cell_value(i+1,n+2))

#myarray=np.asarray(a)
#nn=myarray.reshape((81,2))
#bb=nn.tolist()

zz=np.arange(162)
newzz=zz[0:162:2]
    
coordinate_array=np.zeros((sheet.nrows-1,sheet.ncols-2))
for i in range(sheet.nrows-1):
    for n in range(sheet.ncols-2):
            coordinate_array[i,n]=a[newzz[i]+n]
            
#print(coordinates_array)
            
loc = ("C:/Users/asus/Desktop/phyton_final/distancematrix.xls")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
print('number of rows='+str(sheet.nrows))
print('number of columns='+str(sheet.ncols))

dis=[]
for i in range(84):
    dis.append(sheet.row_values(i))
    
dis.pop(2)
dis.pop(1)
dis.pop(0)


for n in range(81):
    
    dis[n].pop(1)
    dis[n].pop(0)
    dis[n][n]=5000


distance_array=np.zeros((sheet.nrows-3,sheet.ncols-2))

for i in range(sheet.nrows-3):
    for n in range(sheet.ncols-2):
            distance_array[i,n]=dis[i][n]
#print(distance_array)
            
xx = coordinate_array[:,0]
yy = coordinate_array[:,1]            
points=xx,yy
myarray=np.asarray(points)            

def route():
    n=len(xx)
    l=list(range(1,n))
    np.random.shuffle(l)
    l.insert(0,6)
    randompath=np.append(l,l[0])
    return randompath
    
def route_length(path):
    path = np.append(path,path[0])
    total_length = 0.0
    for i in range(len(path)-1):
        j = path[i]
        k = path[i+1]
        dist = distance_array[j, k]
        total_length += dist
    return total_length

def draw_route(path):
  path_length =route_length(path)
  path = np.append(path,path[0])
  y = yy[path]
  x = xx[path]
  plt.plot(y,x,'-o')
  plt.title(str(path_length))
  plt.axes().set_aspect('equal')  
  
def cross_over(g1,g2, mutation=0.05):
  r = np.random.randint(len(g1)) 
  newg = np.append(g1[:r],g2[r:])    
  missing = set(g1)-set(newg)
  elements, count = np.unique(newg, return_counts=True)
  dupli= elements[count==2]
  dupli_indices=(newg[:, None] == dupli).argmax(axis=0)  
  newg[dupli_indices]=list(missing)   
  if np.random.rand()<mutation:
    i1,i2 = np.random.randint(0,len(newg),2)
    newg[[i1,i2]] = newg[[i2,i1]] 
  return newg

def create_pop(m):
  pop = []
  fitness = []
  for i in range(m):
    gene = route()
    path_length = route_length(gene)
    pop.append(gene)
    fitness.append(path_length)  
  pop = np.array(pop)
  fitness = np.array(fitness)  
  sortedindex = np.argsort(fitness)
  return pop[sortedindex], fitness[sortedindex]

def next_gen(pop):
  popl = []
  fit = []
  f=int(np.sqrt(len(pop)))
  for g1 in pop[:f]:
    for g2 in pop[:f]:   
      x =  cross_over(g1,g2,mutation=0.05)
      l = draw_route(x)
      popl.append(x)
      fit.append(l)
  pop = np.array(popl)
  fitness = np.array(fit)  
  sortedindex = np.argsort(fitness)
  return pop[sortedindex], fitness[sortedindex]
pop, fitness  = create_pop(850)

for i in range(200):
    pop, fitness = next_gen(pop)
    if i%5 == 0:
        print(i)

shortest_path = list(pop[0])
draw_route(shortest_path)
    
    
    
    
    
    
    
    
    
    
    
    
    