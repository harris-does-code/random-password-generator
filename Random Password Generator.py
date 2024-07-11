#!/usr/bin/env python

"""Author: Amber Harris
Project: Random Password Generator
Last date edited: 12/9/2023

The program will generate a password for a user. The user will enter the number of 
lowercase letters, uppercase letters, special characters, and numeric characters 
required for the password. Using the requirements, the program will generate a
password where all characters are random.
"""

import random
import string

#Validation for a 0 or negative number password length.
def password_len_validation():
    accept_length = False
    while not accept_length:
        password_length = int(input('Enter the password length as a whole number:\n'))
        if password_length > 0:
            accept_length = True
        else:
            print('Error! Password length must be greater than 0.')
    return password_length

#Validation for the negative numbers entered for lowercase letters, uppercase letters, special characters, and numeric characters.
def lowercase_validation():
    not_negative_num = False
    while not not_negative_num:
        lowercase_num = int(input('Enter the number of lowercase letters for your password:\n'))
        if lowercase_num >= 0:
            not_negative_num = True
        else:
            print('Error! The number entered cannot be negative.\n')
    return lowercase_num

def uppercase_validation():
    not_negative_num = False
    while not not_negative_num:
        uppercase_num = int(input('Enter the number of uppercase letters for your password:\n'))
        if uppercase_num >= 0:
            not_negative_num = True
        else:
            print('Error! The number entered cannot be less than 0.\n')
    return uppercase_num

def specialchr_validation():
    not_negative_num = False
    while not not_negative_num:
        specialchr_num = int(input('Enter the number of special characters for your password:\n'))
        if specialchr_num >= 0:
            not_negative_num = True
        else:
            print('Error! The number entered cannot be less than 0.\n')
    return specialchr_num

def numeric_validation():
    not_negative_num = False
    while not not_negative_num:
        numeric_num = int(input('Enter the number of numeric characters for your password:\n'))
        if numeric_num >= 0:
            not_negative_num = True
        else:
            print('Error! The number entered cannot be less than 0.\n')
    return numeric_num

#Randomly get lowercase letters, uppercase letters, special characters, and numeric characters based on user input.
def get_lowercase(lowercase_num: int):
    lowercase = []
    h = 0

    for h in range(lowercase_num):
        lowercase.append(random.choice(string.ascii_lowercase))
    h += 1

    return lowercase

def get_uppercase(uppercase_num: int):
    uppercase = []
    i = 0

    for i in range(uppercase_num):
        uppercase.append(random.choice(string.ascii_uppercase))
        i += 1
    
    return uppercase

def get_specialchr(specialchr_num: int):
    specialchr = []
    j = 0
    
    for j in range(specialchr_num):
        specialchr.append(random.choice(string.punctuation))
        j += 1

    return specialchr

def get_numeric(numeric_num: int):
    numeric = []
    k = 0
    
    for k in range(numeric_num):
        numeric.append(random.choice(string.digits))
        k += 1

    return numeric

#Provide instructions for user    
print('Please enter your password requirements when prompted.\n')
print('The password length should be a number greater than 0.\nThe total number of lowercase letters, uppercase letters, special characters, and numeric characters must equal the password length.\n')

#Call to validations and store user input for password length and the amount of lowercase letters, uppercase letters, special characters, and numeric characters.
equal_num = False
while not equal_num:
    password_length = password_len_validation()
    lowercase_num = lowercase_validation()
    uppercase_num = uppercase_validation()
    specialchr_num = specialchr_validation()
    numeric_num = numeric_validation()
    sum_inputs = lowercase_num + uppercase_num + specialchr_num + numeric_num
    if sum_inputs == password_length:
        equal_num = True
    elif sum_inputs > password_length:
        print('The total for lowercase letters, uppercase letters, special characters, and numeric characters is greater than the password length entered.\nPlease re-enter the password length and character infromation.')
    else:
        print('The total for lowercase letters, uppercase letters, special characters, and numeric characters is less than the password length entered.\nPlease re-enter the password length and character infromation.')

#Call to get lowercase letters, uppercase letters, special characters, and numeric characters for the password
lowercase = get_lowercase(lowercase_num)
uppercase = get_uppercase(uppercase_num)
specialchr = get_specialchr(specialchr_num)
numeric = get_numeric(numeric_num)

#Join lowercase letters, uppercase letters, special characters, and numeric characters
password_list = lowercase + uppercase + specialchr + numeric

#Randomly shuffle password characters
random.shuffle(password_list)

#Ensure characters next to each other are not equal, and if so, move one character to the end of the list
iter_list = iter(password_list)

i = 0

while i <= len(password_list):
    for x in range(0, len(password_list), 2):
        if x == next(iter_list, len(password_list)):
            password_list.append(password_list.pop(password_list.index[-1]))
    i += 1

#Convert the list to a string
password = ''.join(password_list)

#Output password for user
print(password)
