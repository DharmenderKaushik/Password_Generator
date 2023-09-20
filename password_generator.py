# Random Password Generator 
import random
import string
name=input("Enter your name : ")

print(f"Welcome {name} to our password generator program")

def generate_pass():

    pass_length = int(input("Enter the length of password you want: "))
    while True:
        if (type(pass_length) == int and pass_length > 0):
            break
        else:
            print(f"{name} Please Enter valid length ")
            pass_length = int(input("Enter the length of password you want: "))

    lower_data = string.ascii_lowercase
    upper_data = string.ascii_uppercase
    digits_data = string.digits
    symbols_data =string.punctuation

    # Password have data with lower,upper,digit and symbols:
    data = lower_data + upper_data + digits_data + symbols_data

    generated_pass_list =random.sample(data, pass_length)

    #converting generated list into String :
    generated_password = "".join(generated_pass_list)
    print(generated_password)


generate_pass()