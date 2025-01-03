import numpy as np


x = np.array( [1,2,3] )
print( x * 3 )


#In mathematics x + 3 is impossible(but we can make it possible through multiplying by an identity matrix) but in numpy it become possible because of broadcasting

print( x + 3 ) # 3 is broadcasted over x because it is following rule 2...

#General rules : Two dimensions are compatible when 
#-- they are equal , or
#-- one of them(dimension) is 1


x = np.arange(4) #returns Rank-1 tensor...
xx = x.reshape(4,1) # now x becomes column vector...
y = np.ones(5)
z = np.ones((3,4))

print("x = " , x )
print("xx = " , xx )
print("y = " , y )
print("z = " , z )

print("Shapes: ")
print(x.shape) # Rank-1 tensor
print(xx.shape) # column vector
print(y.shape) # Rank-1 tensor
print(z.shape) # matrix(2D)

#x =  [0 1 2 3]
# xx =  [[0]
#  [1]
#  [2]
#  [3]]
# y =  [1. 1. 1. 1. 1.]
# z =  [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
# Shapes:
# (4,)
# (4, 1)
# (5,)
# (3, 4)

# print( x + y ) 
# does not work because x has shape (4,) and y has (5,) so neither of them has same shape nor 1
#Error(it is not saying that addition isn't possible)
#operands could not be broadcast together with shapes (4,) (5,)  

print( xx + y )
# works because xx has shape (4,1) and y has shape (5,) so they follows rule 2 
##xx is broadcasted over y because xx has second dimension 1 
# [[1. 1. 1. 1. 1.]
#  [2. 2. 2. 2. 2.]
#  [3. 3. 3. 3. 3.]
#  [4. 4. 4. 4. 4.]] 
print( (xx + y).shape) #(4, 5) xx have 4 rows and y have 5 columns !!
print(np.array([1]) + y) # because np.array[1] returns Rank-1 tensor this means it can broadcast over y,x,xx etc.

## z =  [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
#x =  [0 1 2 3]
print( z + x ) # work because z has shape (3,4)
# and x has shape (4,) so they have same dim ... 

#In same dimension complete vector broadcasted 
# If one dimension is 1 so in that case an element broadcasted...

y = np.ones( (3,4) )
r = np.ones( (4) )
print( r )
print( y )

a = np.array( [ [ 0.0 , 0.0 , 0.0 ],
               [ 10.0 , 10.0 , 10.0 ],
               [ 20.0 , 20.0 , 20.0 ],
               [ 30.0 , 30.0 , 30.0 ] ] )
               
b = np.array( [ 1.0, 2.0, 3.0 ] )
print(b.shape)

print( a + b )


a = np.array( [ [ 0.0 , 0.0 , 0.0 , 0.0 ],
               [ 10.0 , 10.0 , 10.0 , 10.0 ],
               [ 20.0 , 20.0 , 20.0 , 20.0],
               [ 30.0 , 30.0 , 30.0 , 30.0 ] ] )
               
b = np.array( [ 1.0] )
x = b.reshape(1,1)
print(x.shape)


#here a + b doesn't work bcz of they having not same dims as well as no one of them has one dim 1

print( a + x )

a = np.array( [ 0.0 , 0.0 , 0.0 , 0.0] )
b = np.array([ 1.0 , 2.0 ,3.0 ])
# print( a + b )

a1 = b.reshape(3,1)
print(a1,a)
print( a1 + a )

 