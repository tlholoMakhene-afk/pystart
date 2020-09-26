msg = "Hello World"
print(msg)

file = open ("./New folder/mylife.txt", "r")
#r is for reading, w is for writing and a for appending
#these are file opening modes
print(file.name)
#this function/property returns a string which is the files name
print(file.mode)
#show us the mode used
#always close your file using the close method
file.close()

with open ("./New folder/mylife.txt", "r") as File1:
    Stuff_in_file=File1.read()
    print(Stuff_in_file)
print(File1.closed)
print(Stuff_in_file)

with open ("./New folder/mylife.txt", "r") as ReadingEachLine:
    Stuff_in_file=ReadingEachLine.readlines()
    print(Stuff_in_file[0])
    
    print(Stuff_in_file)

