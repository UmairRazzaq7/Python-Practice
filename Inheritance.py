#Create a base class Person with attributes name and age.
#  Derive a class Student that adds student_id and a method display() to show all info.

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nStudent_id: {self.student_id}")


s= Student("Ali",20,52)
s.display()



#Vehicle has brand and color. Car inherits and adds model and year.
#  Create a method to show full details.

class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    
class Car(Vehicle):
    def __init__(self,brand,color,model,year):
        super().__init__(brand,color)
        self.model = model
        self.year = year

    def show_details(self):
        print(f"Brand :{self.brand}\nColor :{self.color}\nModel :{self.model}\nYear :{self.year}")

c1 = Car("Zuzuki","White",26,2026)
c1.show_details()
  


#LivingBeing has is_alive = True. Animal adds can_move().
#  Bird adds can_fly = True. Print all inherited features.


class LivingBeing:
    def is_alive (self):
        return True
    
class Animal(LivingBeing):
    def can_move(self):
        return True
    
class Birds(Animal):
    def can_fly(self):
        return True
    def details(self):
        print(f"is_alive:{self.is_alive()}")
        print(f"can_move:{self.can_move()}")
        print(f"can_fly:{self.can_fly()}")
    
parrot = Birds()
parrot.details()



#University has name. Faculty adds department.
# Professor adds subject. Show full details of a professor.

class University:
    def __init__(self,name):
        self.name = name

class Faculty(University):
    def __init__(self,name,department):
        super().__init__(name)
        self.department = department

class Professor(Faculty):
    def __init__(self,name,department,subject):
        super().__init__(name,department)
        
        self.subject = subject

    def prof_details(self):
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")
        print(f"subject : {self.subject}")

details = Professor("Arif Khalil","IOP","Solid State Physics")
details.prof_details()



#Mother and Father both have different attributes.
#  Child inherits and shows combined info.

class Mother:
    def art(self):
        print("Painting")

class Father:
    def skill(self):
        print("Cricket")

class Child(Mother,Father):
    pass

c = Child()
c.art()
c.skill()


    


