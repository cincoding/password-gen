import string
import random

# characters to generate passwords from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_pwd():
    # length of password from the user
    length = int(input("Enter password length: "))

    # number of character types
    alphabets_count = int(input("Enter the amount of alphabets needed in password: "))
    digits_count = int(input("Enter the amount of digits needed in password: "))
    special_characters_count = int(input("Enter the amount of special characters needed in password: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    # check the total length with character sum count
    # print not valid if the sum is greater than length
    if characters_count > length:
        print("Characters total count is greater than the password length")
        return
    
    # intializing the password
    password = []

    # picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    # picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))

    # picking random special character
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    # if the total characters count is less than the password than the password length
    # add random characters characters to make it equal to the length
    if characters_count < length:
        random.shuffle(characters)

    for i in range(length - characters_count):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generate_random_pwd()
