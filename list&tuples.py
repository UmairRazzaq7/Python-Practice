#Remove all duplicates from a list while maintaining order.

list = [1,2,3,2,4,5,6,7,4]

#set has unique characters
remove_dup = set(list)

print(remove_dup)


#Count how many times a specific element appears in a list.

list = [1,2,3,4,2,4,5,2,4,2,5,2]

element = list.count(2)

print(element)


#Convert a list to a tuple .

list = [1,2,3,4,5,6]

listintotuple = tuple(list)

print(listintotuple)



#Create a list of squares of numbers from 1 to 20.

squares = [x**2 for x in range(1,21)]

print(squares)


#Extract all words longer than 5 letters from a given sentence.

text = "Python is really fun to learn and practice"

long_words= [word for word in text.split() if len(word)>5]

print(long_words)
                 

#Given a list of names, return a list of those starting with 'A' or 'a'.
names = ["Umair","Ali","ahmad","hassan","Amir"]

a_names = [name for name in names if name.startswith('A') or name.startswith('a')]

print(a_names)
        