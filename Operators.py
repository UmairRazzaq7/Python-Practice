#Arithematic Operators
#Take two numbers as input and print their sum, difference, product, and quotient.

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

#define parameters

sum = a+b
difference = a-b
product = a*b
quotient = a/b

#to get output

print("Sum = " ,sum)
print("Difference = ",difference)
print("Product = ", product)
print("Quotient = ",  quotient)



#Comparison Operators
# Take a number and check if it’s positive, negative, or zero using only comparison operators.

a = int(input("Enter a number : "))

#Conditions for comparison
if a > 0:
    print("The number you entered is Positive.")
elif a < 0:
    print("The number you entered is negative.")
else:
    print("The number you entered is Zero")


#Logical Operators 
#Ask the user for age and nationality. Allow voting only if age ≥ 18 and nationality is "Pakistani"

age = int(input("Enter your age : "))
nationality = input("Enter your nationality: ")

#define logic

if age >= 18 and nationality == "Pakistani":
    print("You are eligible to vote...")

else:
    print("You are not eligible for vote...")


#Assignment Operators
#Start with x = 50. Apply  += , then *= , then  -= . Print final value.

x = 50

x += 10
x *= 2
x -= 30

print('Final Value of X = ',x)


#Bitwise Operators
#Use bitwise AND to check if a number is even or odd.

num = int(input("Enter a number : "))

#And Operator

if num & 1:
    print("The number is Odd")
else:
    print("The number is Even")



