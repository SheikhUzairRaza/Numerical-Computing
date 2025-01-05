import numpy as np; import matplotlib.pyplot as plt


i = np.array([
    [ [0.1, 0.1 , 0.9] ,[0.2, 0.1, 0.9] ,[0.3, 0.1, 0.9] ],
     
     [ [0.1, 0.2 , 0.9] ,[0.2, 0.2, 0.9] ,[0.3, 0.2, 0.9] ], 
    
     [ [0.1, 0.3 , 0.9] ,[0.2, 0.3, 0.9] ,[0.3, 0.3, 0.9] ],
    
     [ [0.1, 0.4 , 0.9] ,[0.2, 0.4, 0.9] ,[0.3, 0.4, 0.9] ]      
]) # 3d tensor 

print(i.shape) # (4,3,3) # this is what an image looks like to a computer  #rows,column,and pixel(rgb)

(plt.imshow(i)) ## Display the 3D tensor as an image
# plt.show() # Show the plot (Towards right in first row red color is increasing and downwards green color)
print(i.reshape(36,1)) # we get a col. vector
# here we have to multiply by ourselves converting into an automation

i_sh = i.shape
i.reshape(i_sh[0]*i_sh[1]*i_sh[2],1)
# Also known as "flattening" in ML