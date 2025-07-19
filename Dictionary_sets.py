#Create a dictionary with keys 'name', 'age', and 'city', and assign some values.

dict = {
    'name' : "Umair",
    'age'  : 19  ,
    'city' : "Multan"
}


print(dict)


#Nested Dictionary Access
#Acces city


data = {"person":
         {"name": "Ali",
           "info": {"age": 21, 
                    "city": "Lahore"}
         }
        }


print(data["person"]["info"]["city"])



#Convert two lists keys = ['a', 'b'] and values = [1, 2] into a dictionary.

keys = ['a', 'b']
values = [1, 2]

my_dict = dict(zip(keys,values))

print(my_dict)


#Remove duplicates from ["a", "b", "a", "c", "b"].

list =  ["a", "b", "a", "c", "b"]

remove_dup = sorted(set(list))


print(remove_dup)



#Add 'grape' to a set and remove 'orange'.


set = {"apple","orange","cherry","banana"}

set.remove("orange")
set.add("grape")

print(set)



#Find common elements in A = {1,2,3} and B = {2,3,4}.

A = {1,2,3}
B = {2,3,4}

common_ele = A.intersection(B)

print(common_ele)


#Check if {1,2} is a subset of {1,2,3,4}.

A = {1,2,3,4}
B = {1,2}

check = B.issubset(A)

print(check)