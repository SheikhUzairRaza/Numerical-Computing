x=5 #basic datatype revision why data type should be defined for compiler easiness!

#fn and fn importance

def good_enough(x,guess):
    return abs((guess*guess)-x)<0.00000000001

def improve_guess(x,guess):
    return (guess+x/guess)/2

def sqrt(x,guess=0.0001):
    if good_enough(x,guess):
        return guess
    else:
        return sqrt(x,improve_guess(x,guess))
print(sqrt(36))


#while loop

p=0
while(p<10):
    print(p)
    p+=1

#for loop
for i in range(10):
    print(i)

#list (like linkedList b/c insertion deletion size grow/decrease as input increase)

L=[1,2,4]

for i in [1,2,5]:
    print(f"Square Root of {str(i)} : ",  end='')
    print(sqrt(i))

d={
    1:"one",
    2:"two"
}
#words->keys,meanings->pair

print(d[1])
print(d.items())

for key,value in d.items():
    print(f"{key} is {value}")

print(list(d.keys()))


a=[1,2,3,4,5]
b=[6,7,8,9,0]

merged=list(zip(a,b))
print(merged)


##real-world implementation

fields=["id","name","location"]
values=["13","bill","redmond"]
dict(zip(fields,values))




