#!/usr/bin/python

# Code always runs top to bottom. Comments are designed to add notes to your code
# like this. You are reading a comment right now. Comments in python start with
# hashtags
print("Hello World")


#----------------------------------------------------------------------
# Lets try printing a number:
# Let's make a a variable called x and assign it the number 5
x = 5

# For this print statment, we say x is an argument of print()
print(x)

#-----------------------------------------------------------------

# Notice the spacing of the output when you run this line to print 2 arguments:
print("Hello World", x)


# Step 2 
# Data Types - String, int, float
string = "5.0"
interger = 5
float = 6.23

# We can use the built-in type() to find out the data type:
print(float, "is", type(float))
print(string, "is", type(string))

# -------------------------------------------------------------------
# We can print both at the same time with a space in between like this:
print(string, float)

# Say we want to have more customizaion - No spacing or custom spacing:
# We use + to do whats called "concatinate" aka - combine two elements
print("String 1" + "String 2")
print("String 1 " + "String 2")
print("String 1"+ " String 2")
print("String 1" + " " + "String 2")

# ------------------------------------------------------------------
# Lastly Try this:
print(string + float)
# This fails because concatination only works for the same type

# --------------------------------------------------------------------
# Convert one type to another - we call it casting
print(string + str(float))

