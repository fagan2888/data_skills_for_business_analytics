def int_or_not():
    string = input("Please Enter a String: ")
    if string.isdigit():
        print("This is an integer.")
    else:
        print("This is not an integer.")

def remove_char(string,index):
    if string:
        print(string[:index] + string[index + 1:])
    else:
        print("Non-Empty String")

def add_ing(string):
    if len(string) < 3:
        print(string)
    elif string[-3:] == "ing":
        print(string+"ly")
    else:
        print(string+"ing")

def first_half(string):
    print(string[:int(len(string)/2)])

def create_account():
    confirmed, usrname_confirmed, passwrd_confirmed = 0, 0, 0
    while not confirmed:
        usrname = input("Enter Username: ")
        pasword = input("Enter Password: ")
        #________________Username Test________________#
        if usrname[0].isalpha() and usrname.isalnum() \
        and (len(usrname) >= 6 and len(usrname) <= 12):
            print("Username Confirmed!")      
            usrname_confirmed += 1

        #________________Password Test________________#
        uppr = [x for x in pasword if x.isupper()]
        temp = ''.join(char for char in pasword if char not in "@_$%")
        if pasword[0].isalpha() and temp.isalnum() \
        and (len(pasword) > len(temp)) and len(uppr) > 0:
            print("Password Confirmed!")
            passwrd_confirmed += 1

        #_______________Confirming Test_______________#
        if usrname_confirmed and passwrd_confirmed:
            confirmed += 1
        elif not confirmed:
            print("Try Again, Not Meeting Requirements ")
    print("Success, Account Created!")