# Day 5
# Beginner - Python Loops

import numpy as np

# for item in list_of_items:

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)

# for item in list_of_items append a word
for fruit in fruits:
    print(f"{fruit} pie")

# write a program that calculates the average student height from a list of heights
# can't use sum() or len()

student_heights = [180, 124, 165, 173, 189, 169, 146]

def get_number_of_elements(list):

    count = 0
    for i in list:
        count += 1
    return count

def sum_elements_in_list(list):

    total = 0
    for i in list:
        total +=  i
    return total


def get_avg_heights(list):
    avg = sum_elements_in_list(list) / get_number_of_elements(list)
    print(avg)
    return avg

get_avg_heights(student_heights)

# write a program that calculates the max student height from a list of heights

def get_max(list):
    _max = 0
    for score in student_heights:
        if score > _max:
            _max = score
    print(_max)
    return _max

get_max(student_heights)

# write a function that adds all the numbers between 1 and 100

total = 0
for number in range(1, 101):
    total += number
print(total)

# write a function that adds all the even numbers between 1 and 100

total = 0
for number in range(1, 101):
    if (number % 2) == 0:
        total += number
print(total)
    
#  A program that prints the numbers from 1 to 100. But for multiples of
#  three prints "Fizz" instead of the number and for the multiples of five print
#  "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

import random
from random import sample

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Create a password generator

print('Welcome to the PyPassword Generator!')

# letters is knowingly not A:Z
letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all = letters + numbers + symbols

nbr_letters = int(input('How many letters would you like in your password? '))
nbr_numbers = int(input('How many numbers would you like in your password? '))
nbr_symbols = int(input('How many symbols would you like in your password? '))

password_list = []

for char in range(1, nbr_letters + 1):

    # password_list.append(random.choice(letters))
    password_list += random.choice(letters)

for char in range(1, nbr_numbers + 1):

    password_list += random.choice(numbers)

for char in range(1, nbr_symbols + 1):

    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ''

for char in password_list:
    password += char

print(f'Your password is: {password}')