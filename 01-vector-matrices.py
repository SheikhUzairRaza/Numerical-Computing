class Vector:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"[{{{str(self.x)}}},{{{str(self.y)}}}]"


a = Vector(2,4)
print(a)


b= Vector(3,5)
print(b)


def add(self,b):  #if b is defined as a vector it would be more better!
    c = Vector()
    c.x = self.x + b.x
    c.y = self.y + b.y
    return c

Vector.add = add 

c = a.add(b)
print(c)

def mul(self,s): #multiplication is done with a scalar
    d = Vector()
    d.x = self.x * s
    d.y = self.y * s
    return d

Vector.mul=mul
   
d = a.mul(3)
print(d)


def sub(self,b):
    return self.add(b.mul(-1))

Vector.sub = sub


# trying to make it closer to maths but Julia popularity has one of its reason is 


d_min_b = d.sub(b)


## TODO : DEFINE Dot and Cross Product:

def Dot_Product(self,d): 
    return (self.x * d.x + self.y * d.y)

Vector.Dot_Product = Dot_Product

a_dot_b = a.Dot_Product(b);
print(a_dot_b)

def Cross_Product(self,c):
     return (self.x * c.y - self.y * c.x)
Vector.Cross_Product = Cross_Product

a_cross_b = a.Cross_Product(b);
print(a_cross_b)



# GeoGebra S/W for vector visualization