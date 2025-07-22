#Duck Typing (Dynamic Typing)

class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

animal_sound(dog)   
animal_sound(cat)  
#(Even though dog and cat are different classes, 
# the function animal_sound() works for both because they both implement .speak() method.)







#Method Overriding (Run-time Polymorphism)
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# List of shapes
shapes = [Square(4), Circle(3)]

for shape in shapes:
    print(round(shape.area(),2))
  






#Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)   




