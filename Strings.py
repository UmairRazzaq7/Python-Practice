#Check if a string is palindrome.


def is_palindrome(s):
    s=s.lower()
    return s == s[::-1]

word = input("Enter a string : ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")



#Replace all vowels in a string with *.


def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

str = "Hello , this is Umair."
result = replace_vowels(str)

print(result)
 


#Print every 2nd character from a string using slicing.


str = ("length","mass","time","temperature","Intensity","mole") 

result = str[::2]

print(result)


#Extract the middle three characters from a string of odd length.


str = ("apple","orange","banana","apricot","mango","peach","cherry")

mid = len(str)//2

mid3 = str[mid-1:mid+2]
print(mid3)



#Given a string of words, reverse the order of words.

str = "I am a Pakistani . I live in capital city"

reverse_str= str.split()[::-1]


print(reverse_str)