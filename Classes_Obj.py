#Create a class Student with attributes name and age. Add a method display() to print the details.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def display(self):
        print(f"Name of student : {self.name}")
        print(f"Age of student : {self.age}")

s1 = Student("Umair",19)
s1.display()


#Create a class Circle with a method to calculate and return the area.


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(round(3.14*self.radius*self.radius,2))

c = Circle(3)

c.area()
        


#Create a class BankAccount with methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self,amount):

        self.amount = amount
        
    amount = 0
    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount")
        else:
            self.amount += amount
            
            print(f"{amount} deposited successfully.")
        
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount.Enter amount in multiple of 500")
        else:
            self.amount -= amount
            print(f"{amount} withdrawn successfully.")
        
    def check_balance(self):
        return self.amount
    
balnc = BankAccount(10000)

balnc.deposit(500)

c = balnc.check_balance()
print(f"Updated Balance : {c}")

balnc.withdraw(2000)

c = balnc.check_balance()
print(f"Ramining Balance : {c}")


#Create a class Calculator with methods for add, subtract, multiply, and divide.

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
            return self.x+self.y
    
    def subtract(self):
          return self.x-self.y
    
    def multiply(self):
         return self.x * self.y
    
    def divide(self):
         return self.x / self.y
    
values = Calculator(4,5)

print(values.add())
print(values.subtract())
print(values.multiply())
print(values.divide())


    
#Create a class Person that has a method is_adult() which returns True if age >= 18.

class Person:
    def __init__(self,age):
         self.age = age
         
    def is_adult(self):
         if self.age >= 18:
              return True
         else:
              return False
         
p1 = Person(17)

print(p1.is_adult())
            
    
