import numpy as np 
M = np.zeros((3,5)) 
print(M)

print(0.)  #0.0

N = np.ones((5,3))
print(N)

A  = np.arange(1,7)
print(A)
#[1 2 3 4 5 6]
print(A.shape) # Rank 1 tensor return


A[3] = 7
print(A)

# A[1]=1
# A[2]=1
# A[3]=1 
A[:3]=1 #from start and till 3(exclusive) and by default step by 1
print(A)

A[1:4] = [9,8,7]
print(A)


A[:-1]=2
print(A)