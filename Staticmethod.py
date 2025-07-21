#Create a class MathTool with a static method add(a, b) that returns the sum of two numbers.
"""
class MathTool:
    @staticmethod

    def add(x,y):
        return x+y
    
res = MathTool.add(5,4)
print(res)

"""

#Create a static method in a class NumberUtils called is_even(n) that returns True if a number is even.
""" 
class NumberUtils:
    @staticmethod

    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
        
check = NumberUtils.is_even(11)

print(check)

"""

#Create a class Validator with a static method is_valid_email(email) that returns True if '@' is in the email string.
"""
class Validator:
    @staticmethod

    def is_valid_email(email):
        if "@"  in email:
            return True
        else:
            return False
        
mail = Validator.is_valid_email("urazaq714@gmail.com")
print(mail)
"""

#Write a class DateUtils with a static method is_leap_year(year) that returns True if it's a leap year.

class DateUtils:
    @staticmethod

    def is_leap_year(year):
        if (year%4==0 and year%100!=0) or year%400==0: #condition for leap year
            return True
        else:
            return False
        
y = DateUtils.is_leap_year(2025)

print(y)