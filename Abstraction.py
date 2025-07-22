#Create an abstract class Shape with an abstract method area(). 
# Then create subclasses Circle and Rectangle and implement the area() method in each.
"""
from abc import ABC ,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    

c = Circle(5)        
print("Area of Circle:",round(c.area(),2))

r = Rectangle(4,6)
print("Area of Rectangle:",r.area())




#Create an abstract class Vehicle with an abstract method start_engine(). 
#Create subclasses Car and Bike with their specific implementation of start_engine().

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self):
        self.acc = False
        self.clutch = False

    def start_engine(self):
        self.acc = True
        self.clutch = True
        print("Car engine started.....")

class Bike(Vehicle):
    def __init__(self):
        self.brk = False
        self.clutch = False
    
    def start_engine(self):
        self.brk = True
        self.clutch = True
        print("Bike engine started.....")

c = Car()
c.start_engine()

b = Bike()
b.start_engine()


"""




#Define an abstract class LoginSystem with abstract methods authenticate() and logout().
#  Implement it in two classes:
#AdminLogin
#UserLogin


from abc import ABC, abstractmethod

class LoginSystem(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class AdminLogin(LoginSystem):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.logged_in = False

    def authenticate(self,input_username,input_password):
        if self.username == input_username and self.password == input_password:
            self.logged_in = True
            print(f"Welcome {self.username}")

        else:
            print("Authentication Failed....")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print(f"{self.username} has been logged out.")

        else:
            print("No User is currently logged in.")


c = AdminLogin("Umair",12345)
c.authenticate("Umair",102345)
c.logout()








        
