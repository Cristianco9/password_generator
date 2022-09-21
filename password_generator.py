import random
import string

def password_generator(character_length):
    character = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    password = []

    while (len(password) < character_length):
        character_storage = random.choice(character)
        password.append(character_storage)

    password = "".join(password)
    return password

def run():

    print("\n****************************************************")
    print("**************** PASSWORD GENERATOR ****************")
    print("****************************************************")
    character_length = int(input("Please define the password length: "))
    password = password_generator(character_length)
    print("Your password of {} characters is".format(character_length))
    print(password)
    print("********************** DONE ************************")
    print("****************** SCRIPT ENDED ********************")
    

if __name__ == '__main__':
    run()
