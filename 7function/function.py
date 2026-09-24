def hi():
    print("hi")

def greet(name):#parameter
    print(f"helllo {name} ")
    

def sum(a, b):
    return a+b

def palindrome(s):
    if(s==s[::-1]):
        
        print("palindrome")
    else:
        print("not palindrome")
        
        
 
def student(name , age):
    print(name , age)
    

    

hi()
greet("akash")#argument
result = sum(4,6) 
print(result)

palindrome("racecar")
palindrome("dalda")
palindrome("akash")


#types of argument
#positioal argumet -> postion matters 
student("akash", 20)
student("34", "kishore")


#keyword argument -> position does not matter

student(age =21 , name = "santosh")

#default argument -> if we do not pass any value then default value will be taken
def student1(name , age = 20):
    print(name , age)
    
student1("akash")  
   
#variable length arguments ->when we dont know how many arguments will be giver

def add(*numbers): #collects in a tupple 
    print(numbers)
    
    
add(1,5,57,45234,5,4)
# ** used for multiple keyword arguments

def person(**details): # collects in dictionary
    print(details)
    
person( name = "Akash" , age = 22, course = "btech" , cgpa = 7)