# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:25:57 2019

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
    
coordinates_array=np.zeros((sheet.nrows-1,sheet.ncols-2))
for i in range(sheet.nrows-1):
    for n in range(sheet.ncols-2):
            coordinates_array[i,n]=a[newzz[i]+n]
            
print(coordinates_array)
            
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
            
print(distance_array)




