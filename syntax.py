import sys
import random
print("Hello, World!")
print(sys.version)

if(5 > 2):
    print("5 is greater than 2")
if 5 > 2:
    print("5 is still greater than 2")
    
# This is a comment
print("Comments are fun!")  # This comment is after code
#print("This is a backslash: \\")

'''this is a
multi-line comment  
using triple single quotes'''

# variable declaration
x = 5
y = "Hello"
print(x)
print(y)

y = 6
x = "World"
print(x)
print(y)    

# Get datatype of variable
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x=y=z="Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)        
print(z)

def myFunc():
    print("python " + x)
    
myFunc()


def myFunc2():
    global nameVar
    
    nameVar = "John"
    print("Hello " + nameVar)
myFunc2()
print(nameVar)

print(random.randrange(1, 10))

# multi-line string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

for x in "banana":
    print(x)
    
    
# check string in string
txt = "The best things in life are free!"
print("free" in txt)

if "best" in txt:
    print("Yes, 'best' is present.")
    
    
#  not in
txt = "The best things in life are free!"
print("expensive" not in txt)

# slicing
b = " Hello, World! "
print(b[2:5])
print(b[0:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
# python strings mod
print(b.upper())
print(b.lower())
print(b.strip()) # removes whitespace
print(b.replace("H", "J"))
print(b.split(",")) # returns [' Hello', ' World! ']

# formatted string
age = 36
txt = f"My name is John, and {age} am {age}"
print(txt.format(age, age))
