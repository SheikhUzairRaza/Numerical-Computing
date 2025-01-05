import numpy as np 
x = np.array([ [ 0 , 3 , 4 ] , 
     [ 1 , 6 , 4 ] ]) 

x_norm = np.amax(x) #get overall max
x_norm = np.amax(x,axis=1)
print(x_norm.shape) #prints [4 6]
# print(x/x_norm) # error ValueError: operands could not be broadcast together with shapes (2,3) (2,)   
x_norm = x_norm.reshape(2,1)
print(x,x_norm)
print(x/x_norm)


# we can also use another normalization method 

# no need to reshpae again

x_norm = np.linalg.norm(x,ord = 2,axis = 1 ,keepdims = True)
print(x_norm)
print(x/x_norm)
help(np.linalg.norm)