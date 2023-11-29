#finding neighbours
import numpy as np
a =np.array([[1, 2,2,5,8],
            [5,6,7,9,3],
            [3,8,9,6,1],
            [4,8,3,1,8],
            [3,7,9,8,5]])
print(a)
b = int(input("enter the row: "))
c = int(input('enter the column: '))
print('Pixel is',a[b,c])
N4=[]
if b-1>=0:
    N4.append(a[b-1,c])
if c+1<5:
    N4.append(a[b,c+1])
if b+1<5:
    N4.append(a[b+1,c])
if c-1>=0:
    N4.append(a[b,c-1])
print('N4:',N4)

N8=[]
if b-1>=0:
    N8.append(a[b-1,c])
if c+1<5:
    N8.append(a[b,c+1])
if b+1<5:
    N8.append(a[b+1,c])
if c-1>=0:
    N8.append(a[b,c-1])
if b-1>=0 and c+1<5:
    N8.append(a[b-1,c+1])
if b-1>=0 and c-1>=0:
    N8.append(a[b-1,c-1])
if b+1<5 and c+1<5:
    N8.append(a[b+1,c+1])
if b+1<5 and c-1>=0:
    N8.append(a[b+1,c-1])
print('N8:',N8)

ND=[]
if b-1>=0 and c+1<5:
    ND.append(a[b-1,c+1])
if b-1>=0 and c-1>=0:
    ND.append(a[b-1,c-1])
if b+1<5 and c+1<5:
    ND.append(a[b+1,c+1])
if b+1<5 and c-1>=0:
    ND.append(a[b+1,c-1])
print('ND:',ND)