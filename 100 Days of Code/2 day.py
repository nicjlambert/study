# Day 2
# Beginner - Understanding Data Types and How to Manipulate Strings

string = "Welcome to the tips calculator!"

print(string)

# first character
print(string[0])

# last character
print(string[len(string) - 1])

# string
print("123" + "345")

# int
print(123 + 345)

# float 

3.14159

# boolean

True
False

# Type error, Type checking and Type Conversion

num_char = len(input("What is your name?"))
#print("Your name has " + num_char + " characters.")
#TypeError: can only concatenate str (not "int") to str
print("Your name has " + str(num_char) + " characters.")

print(type(num_char))


# Data Types: write a script that takes any two digit number and adds the digits together

two_digit_number = input()

print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Mathematical Operations in Python

3 + 5
7 - 4
3 * 2
print(type(6 / 3)) # division will result in a float data type
print(2 ** 2) # exponentiation

# PEMDASLR
# Parentheses
# Exponents
# Multiplication and Division
# Addition and Subtraction
# Left to Right

print(3 * 3 + 3 / 3 - 3)

# reordering the operations
print(3 - 3 / 3 * 3 + 3)

# BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2

print(int(bmi))

# Number manipulation and F strings in Python

print(8 / 3) # 2.6666666666666665
print(round(8 / 3)) # 3
print(round(8 / 3, 2)) # 2.67
print(8 // 3) # 2
print(type(8 // 3)) # <class 'int'>
print(type(8 / 3)) # <class 'float'>

result = 4 / 2
result /= 2
print(result) # 1.0

score = 0
height = 1.8
isWinning = True

# f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Number Manupulation and F strings in Python

print(type(4 / 2))

result = 4 / 2
result  /= 2

score = 0

# User scores a point
score += 1
print(score)

# f-String
print(f"Your score is: {score}, and your result is {result}")

# Life in weeks

age = int(input("What is your current age in years?"))

print(f"You have {(90 - age ) * 52} weeks left.")

# Tip Calculator

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("How percentage of tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))

print(f"Each person should pay: { round((bill + (bill * (tip/100))) / people,2) }")