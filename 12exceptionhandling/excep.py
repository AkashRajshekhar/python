# by exception handling we dont handle syntax errors , indentation  errors , and tab errors 



try:
    n = int(input("enter the value of n:-"))
    print(10/n)

except Exception as err:
    print(f"sorry their is an error as {err} ") 


else:
    print("good there is no excepttion ")
    
finally:
    print("runs forverr") 
    
    
# raise:->manually throw exception 

age = -2
if age <0 :
    raise ValueError("age is negatiive")
    