import sys
print(sys.float_info)

import numpy as np 

#Spacing tells us how far "next largest/smallest" number is...
print(np.spacing(100_000_000))  
print(np.spacing(100.2)) 
#either we have a lot of precision or a very large number...


np.spacing(0.1002) #smaller spacing at this point
