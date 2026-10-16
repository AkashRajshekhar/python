#oops in python 
student1 = ["madhav", 10]
student2 = ["akash", 15]  #if we have 1000students dataa  it is most efficient method to store 
#efficient way is oops 

print(student1)
print(student2)

#class - blueprint or template


class Student:
    def __init__(self, name ,grade ,percentage): #constructor , value 
        self.name= name  #self use to give refrence  fixed 
        self.grade = grade #attribtes 
        self.percentage = percentage
        
        
    def student_detail(self):
        print(f"{self.name} is in class { self.grade} with  {self.percentage}%")   


#object - instance of class
s1 = Student("madhav"  ,11 , 70)
print(s1.name)
print(s1.grade)
s1.student_detail()


#object operations modifying or deleteing
print(s1.percentage)
s1.percentage = 93
print(s1.percentage)


del s1.percentage
#print(s1.percentage)
print(s1)


#abstraction  ->hiding unncessary things from user and provide only useful things 

class Animal:
    def __init__(self , name , activity):
        self.name = name
        self.activity = activity
    
    def details(self): #this method shows abstraction 
       return print(f"{self.name} {self.activity}")



dog = Animal("dog " , "barks"); 
dog.details(); 



class Car:
    def start(self):
        self.__check_engine()
        self.__start_engine()
        print("Car started")

    def __check_engine(self):
        print("Checking engine...")

    def __start_engine(self):
        print("Starting engine...")


car = Car()
car.start()



#Encapsulation -> wrap the whole attribute and method inside a single class and controlling access to that data 


# __ -> limits access
class BankAccount:
    def __init__(self , balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance+=amount
        
        
    def withdraw(self , amount):
        self.__balance-=amount
        
    def show_balance(self):
        print(f"Balance : {self.__balance}")
        
        
account = BankAccount(1000)

# account.__balance()   #give error it can not access directly 
account.deposit(600)
account.withdraw(400)
account.show_balance()   
            
            
            
#inheritance -> child class accquire the attributes and method of parent class 
        


# Parent class
class Animal:

    # Constructor of the parent class
    def __init__(self, name):
        self.name = name  # Store the animal's name

    # Method of the parent class
    def eat(self):
        print(f"{self.name} is eating")


# Child class inherits from Animal
class Dog(Animal):

    # Constructor of the child class
    def __init__(self, name, breed):

        # Call the parent constructor to initialize name
        super().__init__(name)

        # Initialize the dog's breed
        self.breed = breed

    # Method to display dog details
    def details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

    # Method specific to the Dog class
    def bark(self):
        print(f"{self.name} is barking")


# Create an object of the Dog class
dog = Dog("Tommy", "Labrador")

# Call the child class method
dog.details()

# Call the inherited parent class method
dog.eat()

# Call the child class's own method
dog.bark()




#polymorphism -> 

#  polymorphism is an OOP concept in which the same method or interface can have different behaviours depending on the object using it.

# Parent class
class Payment:
    def pay(self, amount):
        # Common method for making a payment
        raise NotImplementedError("Child class must implement pay()")


# Child class for UPI payments
class UpiPayment(Payment):
    def pay(self, amount):
        # UPI-specific payment behaviour
        print(f"Paid Rs.{amount} using UPI")


# Child class for card payments
class CardPayment(Payment):
    def pay(self, amount):
        # Card-specific payment behaviour
        print(f"Paid Rs.{amount} using Card")


# This function works with different payment objects
def make_payment(payment_method, amount):
    payment_method.pay(amount)


# Create objects of different classes
upi = UpiPayment()
card = CardPayment()

# Call the same function with different objects
make_payment(upi, 500)
make_payment(card, 1000)

       
        
        

