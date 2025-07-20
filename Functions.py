#Write a function that returns the square of a number.

def square(num):
    return num*num

result= square(7)

print(result)


#Write a function that prints "Hello, [name]" where name is passed as an argument.


def greetings(name):

    print(f"Hello, {name}")


greet = greetings("Umair")

print(greet)



#Write a function that checks whether a number is even or odd.

def checker(num):
    
    if num%2==0:
          return "Even"
    else:
         return "Odd"
        

check = checker(30)

print(check)



#Write a function that accepts a list of numbers and returns a new list with only the even numbers.

def even(lst):

    even_numb = []

    for ele in lst:
        if ele%2==0:
            even_numb.append(ele)

    return even_numb
    
    
result = even([2,3,5,4,6])

print(result)


#Write a function that takes a string and returns True if it’s a palindrome.

def is_palindrome(str):
    
    if str == str[::-1]:
        return  True
    else:
        return  False
    
str = is_palindrome("racecar")

print(str)
    
