# Implementation of relationship between pixels.
import numpy as np
a =  np.array([[1,5,7,8,5],[11,43,8,6,3],[22,57,7,88,9],[44,6,5,44,33],[8,97,55,9,8]])
print('a: ',a)
b = int(input('Enter the row:'))
c = int(input('Enter the column: '))
print('Element is : ',a[b,c])
 
N4=[]
if b+1<5:
    N4.append(a[b+1,c])
if b-1>=0:
    N4.append(a[b-1,c])
if c+1<5:
    N4.append(a[b,c+1])
if c-1>=0:
    N4.append(a[b,c-1])
print('Neighbours are',N4)

N8=[]
if b+1<5 and c+1<5:
    N8.append(a[b+1,c+1])
if b-1>=0 and c+1<5:
    N8.append(a[b-1,c+1])
if b+1<5 and c-1>=0:
    N8.append(a[b+1,c-1])
if b-1>=0 and c-1>=0:
    N8.append(a[b-1,c-1])
print(N8)
