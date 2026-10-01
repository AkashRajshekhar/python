# list -> immutable, ordered, duplicates, heterogeneous
 
tuple = (1,  "a ame" , "sambhu " , 4.4 , 1 , 0.1)
print(tuple)

for i in tuple:
    print(i)
    
print(tuple[2])

for i in range(len(tuple)):
    print(tuple[i])    

print(tuple.count(1))  
print(tuple.index(1))  

#tuple unpacking
a, b,c,d = (1, 2, 3, 4)
for i in (a, b, c, d):
    print(i)
print(type(a))  
b= (2,)
print(type(b))