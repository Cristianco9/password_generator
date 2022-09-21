# Shebang
#!/usr/bin/env python

# Importing 2 modules: 'random' to generete random numbers and 'string' to generete ASCII characters
import random
import string

# Password generator function, take the password length defined by the user as parameter
def password_generator(character_length):

    # This variable storage ASCII characters
    character = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    # This list saves the characters that make up the password
    password = []
    
    # This loop iterates storing random characters
    while (len(password) < character_length):

        # The method 'random.choice' allow saves random characters in a variable
        character_storage = random.choice(character)
        # Add the random characters list to the password list 
        password.append(character_storage)

    # Join all characters in the list in a single string
    password = "".join(password)
    # As function output return the password list 
    return password

# Main function
def run():

    print("****************************************************")
    print("**************** PASSWORD GENERATOR ****************")
    print("****************************************************")
    # Request password length 
    character_length = int(input("Please define the password length: "))
    # Run password generator function
    password = password_generator(character_length)
    # Print user password length
    print("Your password of {} characters is: ".format(character_length))
    # print the password
    print(password)
    print("********************** DONE ************************")
    print("****************** SCRIPT ENDED ********************")
    
# Entry point defined
if __name__ == '__main__':
    run()
