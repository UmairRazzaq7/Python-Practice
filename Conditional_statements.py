#1:Given three numbers, find and print the largest.

a = 50
b = 80
c = 30

#Conditions

if a>b and a>c:
    print(f"a={a} is the largest number.")
elif b>a and b>c:
    print(f"b={b} is the largets number.")
else:
    print(f"c={c} is the largest number.")


#2: Find leap year.

year = int(input("Enter the year : "))

if (year%4==0 and year%100!=0) or (year%400==0):
          print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")



#3: Write a program to check if a character entered by the user is a vowel or consonant.

char = input("Enter any character : ").lower()

#defien vowels
vowels = "aeiou"
if len(char) == 1 and char.isalpha():

    if char in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is consonant.")

else:
    print("Invalid Input.Plz enter a valid character...")


#4: Take three angles of a triangle as input and check if the triangle is valid.

ang1 = float(input("Enter 1st angle: "))
ang2 = float(input("Enter 2nd angle: "))
ang3 = float(input("Enter 3rd angle: "))

#Condition for triangle:

if ang1+ang2+ang3 == 180:
    print("It is a Valid triangle.")
else:
    print("It is not Valid triangle.")


#5: Write a program to check if a password meets these conditions:
#At least 8 characters
#Contains both letters and numbers

password = input("Enter Your Password: ")

has_letter = False
has_number = False

for char in password:
    if char.isalpha():
        has_letter = True
    elif char.isdigit():
        has_number = True

if len(password)>=8 and has_letter and has_number:
    print(f"{password} is a Valid Password...")

else: 
    print(f"{password} is Invalid Password...Try Again")