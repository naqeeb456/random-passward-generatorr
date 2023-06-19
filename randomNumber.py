import random as r
import secrets as sec
import string as s

    
def get_digits():
    return s.digits.strip()

def get_letters():
    return s.ascii_letters.strip()

def get_special_character():
    return s.punctuation.strip()

def get_total_alphabets():
    alphabets = get_digits() + get_letters() + get_special_character()
    return alphabets

# def limit_wraper(fun,limit):
#     num=''
#     for i in limit:
#         num+=fun()
#     return num    

# def randum_number_generator():
#     number=r.choice(get_digits())
#     return number
    
# def random_alpha_letters():
#     alpha=r.choice(get_letters())
#     return alpha

# def random_special_character():
#     special_character = r.choice(get_special_character())
#     return special_character

#to check user is entering Digit and right length greater than 3

# def pswd_length_IsDigit(leng):
#     while leng < 8 :
#         if (type(leng) is int):
#             leng=int(input("Enter Length equal or greater than 8 upto 20 For a Strong Passward"))
#         else:
#             print("Please enter a valid digit number greater \nthan or equal to 8 for Strong passward  ")
 

#this function simply generate random passward 

def simple_random_passward(leng):
    rand_paswd= ''
    for i in range(leng):
        rand_paswd +=''.join(r.choice(get_total_alphabets()))
    return rand_paswd

# minimum pasward length should be 8
# Atleast 1 special character
# Atleast 3 digits   

def Constraint_random_pasward(leng):
    digits=get_digits()
    sp_ch=get_special_character()
    pasward=''
    while True:
        pasward=str(simple_random_passward(leng))
        if (any(value in sp_ch for value in pasward)>=1 and 
            sum(value in digits for value in pasward)>=3):
            return pasward
    
        

def menu():
    print("\n---------Random-Passward-Generator---------\n")
    print("1. Simple Passward Generator\n2.Constraint Passward Generator\n")
    print("Enter your choice(1 or 2):")

def checker(inpt,down_limit,up_limit):
    while int(inpt)<down_limit or int(inpt)>up_limit:
        inpt=input(f"Please enter your choice from {down_limit} to {up_limit}: ")
    return inpt

def selecte_generator(inpt,leng):
    
    if (inpt==1):
        passward=simple_random_passward(leng)
        return passward
    elif (inpt==2):
        passward= Constraint_random_pasward(leng)
        return passward
        

if __name__=="__main__":
    menu()
    try:
        inpt=int(input())
    except InputError:
        print("Inout Exception: Non integer is enter ")
    checker(inpt,1,2)
    
    try:
        leng=int(input("Enter the length of passward between 8-20: "))
    except InputError:
        print("Inout Exception: Non integer is enter ")
    
    checker(leng,8,20)
    print(selecte_generator(inpt,leng))