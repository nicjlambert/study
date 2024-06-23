# Day 3
# Beginner - Control Flow and Logical Operators

## Control Flow with if / elif / else

#if condition:
    # do this
#elif condition:
    # do this
#else:
    # do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Odd or Even

# Even numbers can be divided by 2 with no remainder.

a = int(input("Enter a number: "))
if a % 2 == 0:
    print(f"The number {a} is an even number.")
else:
    print(f"The number {a} is an odd number.")

# Nested if statements and elif statements

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# BMI Calculator v2.0
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round(float(weight) / float(height) ** 2,2)

#under 18.5kg/m2 – you are considered underweight and possibly malnourished
#18.5 to 24.9kg/m2 – you are within a healthy weight range for young and middle-aged adults
#25.0 to 29.9kg/m2 – you are considered overweight
#over 30kg/m2 – you are considered obese.

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are considered underweight and possibly malnourished.")
elif bmi < 24.9:
    print(f"Your BMI is {bmi}, you are within a healthy weight range for young and middle-aged adults.")
elif bmi <= 29.9:
    print(f"Your BMI is {bmi}, you are considered overweight.")
else:
    print(f"Your BMI is {bmi}, you are considered obese.")

# Leap Year
