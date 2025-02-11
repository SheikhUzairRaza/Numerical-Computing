import numpy as np, math
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

# A[0]=1
# A[1]=1
# A[2]=1 
A[:3]=1 #(Readability and assign to multiple locations)#from start and till 3(exclusive) and in default case it steps by 1
print(A)

A[1:4] = [9,8,7]
print(A)

# A[1:4] = [9,8,7,1]
# print(A)
#ValueError: could not broadcast input array from shape (4,) into shape (3,)   

A[:-1]=2
print(A) # Assign 2 except last index in array ...

#arange returns Rank 1 tensor and .zeros(dim) and .ones(dim) returns 2D array or matrix 
B = np.zeros((2,2))
B[0,0]=5
B[0,1]=2
B[1,1]=4
B[1,0]=6
print(B)
print(B.shape) 

#Array operations
print(B + 2) #In maths it doesn't makes sense B/c we can't add scalar with matrix But in programming it add 2 in all elements of matrix...
#B + 2  [B doesn't change so it means B + 2 is not an in-place operation which means B + 2 will make a copy of B and then add 2 in all the elements and then return it ... Assume in million By million dense matrix there is a huge proB.]

##?first in maths we multiply it with identity matrix then we can do ...

print(2 * B)
#multiplying matrix(B) with scalar

print( B ** 2) #element-wise square not a matrix-matrix multiplication


print(sum(B))
#3 types of sum possible all values sum possible row-wise or column-wise sum is possible...
#sum(B) will produce column-wise sum
#B.sum() will produce all values sum
#B.sum(axis=0) will produce sum column-wise
#B.sum(axis=1) will produce sum row-wise
print(B.sum())

print(B.sum(axis=0)) 
print(B.sum(axis=1))   


print(B.sum(axis=0).shape) # Rank 1 tensor
print(B.sum(axis=1).shape) # Rank 1 tensor


b = np.array( [ [1,2] , [3,4] ])
d = np.array([ [3,4] , [5,6] ])
print(b)
print(d)

print(b + d)
print(b * d)  #element-wise multiplication

print(b.dot(d))  # matrix-multiplication

print(b ** d) # b elements raised to the exponent d (It is not mat raised to the exponent matrix)

print(b) # Firstly printing b
print(b.T) #Transpose Matrix b...
print(d.T) #Transpose Matrix d...

a = np.arange(1,8)
print(a.shape)
print(a.T)
print(a.shape) 

# print(a.dot(b))

# diff b/w rank 1 tensor and vector
print(a.reshape(7,1).T.shape)
# print(a.reshape(7,1).shape)

#Numpy has "broadcasting" or "mapping function"
print(np.sqrt(36))

# works on both scalars and arrays
x = [1,4,9,16] # Rank-1 tensor
print(np.sqrt(x))

d=[[1,9,25],[4,5,7]]
print(np.sqrt(d))

x = np.array([1,2,4,5,9,3])
print(x>3) #returns a boolean type array
y = np.array([0,2,3,1,10,3])
print( x > 3 ) #returns a boolean type array
print( x > y )

#*Let us assume we want to find employees whose salaries are above 50k...

def basic_sigmoid(x):
    
    """
    
    Compute sigmoid of x.
        
    Arguments:
     
    x -- A scalar
    
    Return :
    
    s -- sigmoid(x)

    """
    
    #e ** (-infinite) = 0
    #e ** (infinite) = infinite
    
    s = 1./(1. + math.e ** (-x))
    return s


help(basic_sigmoid) ## returns docstring

print(basic_sigmoid(-1))
print(basic_sigmoid(0))
print(basic_sigmoid(8)) #when x is tending towards positive infinity or we can say limit x -> infinity (basic_sigmoid) it is 1 
# x=[1,4,6]
# print(basic_sigmoid(x))
# TypeError: bad operand type for unary -: 'list' 
#we can fix the error by iteration(loop),control statements and store it in a list and return that ....

#we can also use numpy array for this purpose
x =  np.array([1,4,6]) #NumPy is intelligent enough to compute e^-x even if x is an array.
print(basic_sigmoid(x))

#Lists and arrays may look similar visually, but internally they are completely different in representation, and their code behavior also differs significantly...

