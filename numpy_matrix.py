import numpy as np
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print (A[1,1])
print (A[1,:])
print (A[:,1])
# 0:2 means 0 and 1, 1:3 means 1 and 2
print (A[0:2,1:3])
# we can also denote 0:2 by :2
print (A[:2, :])
print (A[:,1:])
print (A[1:3,0:2])
A[2,2]=100
A[0:2,0:2]=0
print (A)
print (A. shape)
print (A. size)
#(A. ndim)=2 because A is a 2D array
print (A. ndim)

x = np.array([1, 2, 3, 4, 5, 6])
print(x)
print(x. shape)
B = x.reshape(2, 3)
print(B)
C = x. reshape (3, 2)
print (C)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
D = x. reshape (3,4)
print (D)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
print(A * b)


A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(np.sum(A))
print (np. mean(A))
print(np.max(A))
print(np.min(A))
print(np.sum(A, axis=0))
print(np. sum(A, axis=1))


scores = np.array([
    [80, 90, 85],
    [70, 75, 80],
    [95, 90, 100]
])
print(np. mean(scores, axis=0))
print(np.mean(scores, axis=1))