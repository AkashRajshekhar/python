# set -> unordered, mutable, no duplicates , semihetrogeneous

set = {1, 2, 3, 4, 5,2,5,5 , "aksh"} 

print(type(set))

print(set)

for i in set:
    print(i)

# for i in range(len(set)):
#     print(set[i])  # This will raise an error because sets are not subscriptable

# not subricbale
# print(set[0])  # This will raise an error
print(len(set))    

b= hash("ame")  # hash function is used to get the hash value of an object
print(b)
