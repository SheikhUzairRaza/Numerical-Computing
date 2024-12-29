##basics:

##DENSE

Test1 = [[2.0] for i in range(3)] ##list comprehension
print(Test1)
Test2 = [4]*3
print(Test2)

class Matrix :

    def __init__(self,dims,fill):
        self.rows = dims[0]
        self.cols = dims[1]

        self.A = [
            [fill] * self.cols
            for i in range(self.rows)
        ]

#list of list 
    
#list(A) contains row number of elements
    def __str__(self):
        rows = len(self.A) # Get the first dimension(row)
        ret = ''

        for i in range(rows):
            cols = len(self.A[i])

            for j in range(cols):
                ret += str(self.A[i][j]) + "\t"
            ret += '\n'
        return ret 



M = Matrix((3,4),2.0)
print(M)
N = Matrix((50,50),0.0);
# print(N)

# %time n = Matrix((100,100),0.0);
#Magic command that matrix takes to create 
#Memory Usage(Matrix)
# When we store large datasets into matrix how much time it will be required for this ?
from sys import getsizeof
print(getsizeof(M))
print(getsizeof(N))

from pympler.asizeof import asizeof
print(asizeof(M), asizeof(N))

size = asizeof(N)/(1024*1024)
print("{:.2f} MBs".format(size)) #in MB

#we can get values from our matrix using indices 
# def get(self, i , j):
#     if i < 0 or i > self.rows :
#         raise ValueError("Row index out of range.")
#     if j < 0 or j > self.cols:
#         raise ValueError("Column index out of range. ")
    
#     return self.A[i][j]

# Matrix.get = get


def get(self,i,j):

    if i < 0 or i > self.rows :
        raise ValueError("Row index out of range. ")
    if j < 0 or j > self.cols:
        raise ValueError("Column index out of range. ")
    
    return 0.0 
Matrix.get = get

print(M.get(1,2))


#Sparse

class Matrix2:
    def __init__(self,dims):
        self.rows = dims[0]
        self.cols = dims[1]
        self.vals = {}
        #let's assume that fill is 0 here

    def set(self,i,j,val):
        self.vals[ (i,j) ] = val
    #key is tuple
    
    def get(self,i,j):
        if i < 0 or i > self.rows :
            raise ValueError("Row index out of range.")
        if j < 0 or j > self.cols:
            raise ValueError("Column index out of range. ")
    
        if (i,j) in self.vals:
            return self.vals[(i,j)]
        
    
        return 0.0
        
        


S = Matrix2((5,5))
print(S.vals)
print(S.get(1,1))
S.set(1,2,15.0)
print(S.get(1,2))
# print(S.get(10,2))
print(S.vals)

dim = 5000
Q=  Matrix2((dim,dim))

print((asizeof(Q))/(1024*1024))

#Graphs mostly in sparse representation...