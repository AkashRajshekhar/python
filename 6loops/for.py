# two types - for , while

# for --> when we know the number of iterations
# while --> when we don't know the number of iterations but know where we stop

#for
# range(start , stop , step)
a  = range(1,21,2)

for i in a:
    print(i)


for i in range(1,21):
    print(i)
    
for i in range(16 , 0 , -1):
        print(i)
        
for i in range(-3 , -16 , -1): 
    print(i)       
    
    
    #table
for i in range(5 , 51 , 5):
        print(i)
    
str  = "akashrajshekhar"   
for i in range(len(str)):
    
    print(str[i])
    
for i in str:
    print(i)
    