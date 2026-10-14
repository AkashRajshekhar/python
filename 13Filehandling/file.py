import os
f = open(r"C:\Users\akash\OneDrive\Desktop\python\13Filehandling\ main.txt","r")

# r- read the file 

line1 = f.readline() 
print(line1)
line2 = f.readline()
print(line2)



f.close()
# w- write to the file if not exist then create the file

file = open("write.txt","a")
file.write("\n hey i also learning js by chai with code ")

file.write("\n me to ji chla ")
file.close()



# x- create the file 


#with syntax; 


with open("with.txt","a") as s:
    s.write("\n ye w bar bar phle bala overwrite krta hai   ")
   
   
with open("with.txt", "r") as s:
    
    newdata = s.read()
    print(newdata)
    
    
#delete by os 

    

os.remove("delete.txt")