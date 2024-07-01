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

# Rollercoaster Ticket Price v1.0
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
bmi = round(float(weight) / float(height) ** 2, 2)

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

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Rollercoaster Ticket Price v2.0
# Multiple if statements in succession

bill = 0
height = int(input("What is your height? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N: ")

    if wants_photo == "Y":
        bill += 3
        print("Additional $3 for photos.")
        print(f"You final bill is ${bill}.")
    else:
        print(f"You final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
# Pizza Order Practice

size = str(input("What size pizza do you want? S, M, or L: "))

if size == "S":
    bill = 15
    print("Small pizza: $15")

elif size == "M":
    bill = 20
    print("Medium pizza: $20")
else:
    bill = 25
    print("Large pizza: $25")

add_pepperoni = input("Do you want pepperoni? Y or N: ")

if add_pepperoni == "Y" and size == "S":
    bill += 2
    print("Additional $2 for pepperoni.")
else:
    bill += 3
    print("Additional $3 for pepperoni.")

add_cheese = input("Do you want cheese? Y or N: ")

if add_cheese == "Y":
    bill += 1
    print("Additional $1 for cheese.")

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is ${bill}.")

# Love Calculator

print("The love calculator is calculating your love score.")

name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_names = name1 + name2
combined_names = combined_names.lower()
# create a list of letters
true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]

scoretrue = 0
for i in true:
    count = combined_names.count(i)
    scoretrue += count

scorelove = 0
for i in love:
    count = combined_names.count(i)
    scorelove += count

print(f"Your love score is: {str(scoretrue) + str(scorelove)}.")