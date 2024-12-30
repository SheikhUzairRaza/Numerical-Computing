import numpy as np 

#Reproducibility(Able to produce same result)

np.random.seed(1337) #convention
print(np.random.random(5)) 
np.random.seed(1337) #convention
print(np.random.random(5))


#Basics of Matrices

X = np.array( [1,4,3] )  #(Fixed size,Fixed Datatype(Homogeneous(Efficiency)) Rank 1 Tensor(Just have 1 Dimension)
print(X)

Y = np.array([ [1,4,3],
              [4,2,7]])
print(Y)

print(X.shape) #(3,) this means X has 1 dimension

print(Y.shape)

Z = np.array( [ [1,4,3]  ] )
print(Z.shape)
#Difference b/w Z and X is
#Z is a 2D array with 1 row and 3 column & Z is list of list it is also a row vector 
#X is a 1D array with 3 elements 

z = np.arange(1,2000,1) # start,end(exclusive),step
print(z[:-10])#all values from start till end except last ten ...
print(z[-10:])#last ten values
#z[start:end:step]
print(z.shape)

#practicing np.arange
test3 = np.arange(0.5,12,2)
print(test3)
print(test3.shape)
test4 = np.arange(0.5,12,2).reshape(3,2)
print(test4)
print(test4.shape)


#? matrix = np.arange(1, 26).reshape(5, 5)  # 5x5 matrix
# print(matrix)


#?numpy.linspace() function, which generates an array of equally spaced numbers over a specified range

test5 = np.linspace(3,9,10) 
#Linear(step size is fixed)
#np.linspace() works by dividing the range between start and stop into equal intervals.
#This means 10 numbers will be generated between 3 and 9, evenly spaced.
#Step Size= (stop−start)/( num−1)
#Step Size = (9-3)/(10-1)=0.66

print(test5[1:]) 
# test5[start:end:step] starting from index 1 and end at the last
#usecase 1:Graph Plotting


print(Y)
print(Y[0,1]) #row 0(1st dimension index 0) col 1(2nd dimension column index 1)

print(Y[:,1])

print(Y[:,[1,2]])
print(Y[:,[1,2]].shape)



