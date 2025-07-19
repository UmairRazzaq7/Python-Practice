#Use a for loop and range() to print numbers from 1 to 10.


for x in range(1,11):
      #range(starting point, ending point)
    print(x)


#Use a loop and range() with a step to print even numbers from 1 to 20.

for i in range(2,21,2):

    print(i)
    



#Use a while loop to print a countdown from 5 to 1 and 1 to 5.


#5 to 1
i = 5

while i>=1:
    print(i)
    i -=1

#1 to 5

i = 1
while i<=5:
    print(i)
    i += 1

    


#Print the multiplication table of 7 up to 10.

i = 1

while i<=10:
    print(i*7)
    i += 1

    

#Use a loop to compute the factorial of a number n.

n = int(input("Enter a number : "))

factorial = 1

for i in range(1,n+1):

    factorial *= i

    print(factorial)

    

#Check whether a given number is prime using a loop.

n = 50
is_prime =True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
        break
if is_prime:
    print("Prime number....")
else:
    print("Not Prime number....")




