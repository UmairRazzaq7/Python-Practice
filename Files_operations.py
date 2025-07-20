#To read file content


f = open("file.txt","r")

content = f.read()

print(content)



#to overwrite file

f = open("file.txt","w")

f.write("Previous text remove now every thing will be overwritten with new contents")




#to write at end of file i.e append mode

f = open("file.txt","a")

f.write("\n Now this is a new line in file im appending it")




#to write oneline

f = open('file.txt',"r")
data = f.readline()

print(data)





#with syntax

with open("file.txt", "r") as f:
    data = f.read()
    
    print(data)
    


#to close file

f.close()