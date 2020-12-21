#What are variable in Python? Variables are containers for storing data values.Python has no command for declaring a variable.

#A variable is created the moment you first assign a value to it. 

#For example. 

x = "5"
y = "Johnson"
print(x)
print(y)

#In the above examples. X and Y are varibles with values of 5 and Johnson attached of it repectively. 

# As earlier said, variables does not have a any specific way to define it. See examples below.

carname = "Volvo"
value = " is the best car"
msg = (carname + value)
print(msg)

#Get the Type
#You can get the data type of a variable with the type() function.

#Example
x = 5
y = "John"
z = "5John"
print(type(x))
print(type(y))
print(type(z))

x = "My name is Paul. "
y = "I love visiting the mall. "
z = "At the mall, love buying ice screen, watching movies and playing Games"
f = (x + y + z)

print(f)
print(x + y +z)

x = "an Afrian"

def myfunc():
   y = "I love learning python"
   z = "Python"
   print(z + x + y)

myfunc()

#What is a comment(#) in python? A comment in python is represent by the # symbol. 
#A Comment can be used to explain a peace of code. It can be use to make a puthon code more readable. 
#It can be use to prevent execution when testing python code

#A comment can be deplayed in python code as follows:

# This is a comment <--------- Before a peace of code.
print("Hello world")

print("i love eating piza") #This is a comment <-------- At the end of python code.

#It should be noted that python does not really have a syntax for multi line comments.
# For example python code can also be written on multiple line before a piece of code. 

     #Example: 
#This is a comment
#written in
#more than just one line
print("Hello, World!")

