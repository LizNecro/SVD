# -*- coding: utf-8 -*-
"""SVD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XwEeW-KQgc6aClPg1tHw-NAUb6FtsN3t

## **Import libraries**
"""

from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import matrix_rank

"""## **Find SVD of a matrix**"""

def SVD(A):
  eigvl, eigvt = np.linalg.eigh(A.T@A)
  idx = eigvl.argsort()[::-1] # descending order
  eigvl = eigvl[idx]
  eigvt = eigvt[:,idx]
  #Find singular values
  singular_values=[]
  for i in eigvl:
    if i >0:
      x=np.sqrt(i)
      singular_values.append(x)
  #Find matrix V
  V=eigvt.T
  #Find matrix S
  singular_values=np.array(singular_values)
  S=np.diag(singular_values)
  #Find matrix U
  U=[]
  for i in range(len(singular_values)):
    u=A@V[i].T/singular_values[i]
    U.append(u)
  U=np.hstack(U)
  return U,S,V,singular_values

"""## **Find error**"""

def error(k,r,sv,A):
  a=0
  for i in range(k+1,r):
    a+=sv[i]*sv[i]
  error=math.sqrt(a/A)
  return error

"""## **Import Image**"""

from PIL import Image
anh=Image.open("cat2.jpg")
plt.figure(figsize=(16,8))
plt.imshow(anh)

"""## **Convert to gray-scale image**"""

imgray=anh.convert("LA")
plt.figure(figsize=(16,8))
plt.imshow(imgray)

"""## **Find matrix of image**"""

B=np.array(list(imgray.getdata(band=0)),float)
B.shape=(imgray.size[1],imgray.size[0])
B=np.matrix(B)
B

"""## Rank of matrix B"""

rank=matrix_rank(B)
rank

U,S,V,sv=SVD(B)

j=0
A=0
for i in range(rank):
  A+=sv[i]*sv[i]
for r in (1,2,3,5,10,25,50,150,600):
  e=round(error(r,rank,sv,A)*100,2)
  Xapprox=U[:,:r] @ S[0:r,:r] @V[:r,:]
  plt.figure(j+1)
  j+=1
  img=plt.imshow(Xapprox)
  img.set_cmap('gray')
  plt.axis('off')
  plt.title('r='+str(r)+"  "+"error="+str(e))
  plt.show()

U,S,V,sv=SVD(B)

j=0
A=0
for i in range(rank):
  A+=sv[i]*sv[i]
for r in range(150,160):
  e=round(error(r,rank,sv,A)*100,2)
  if e <10:
    Xapprox=U[:,:r] @ S[0:r,:r] @V[:r,:]
    plt.figure(j+1)
    j+=1
    img=plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('r='+str(r)+"  "+"error="+str(e))
    plt.show()