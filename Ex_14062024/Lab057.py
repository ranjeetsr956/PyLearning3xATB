# Functions & match case

def allowed_to_attend_Python_class(name, password):
    match name:
        case "Pramod":
            if password == 123:
                print(name, "You are allowed ")
            else:
                print(name, "You entered wrong password")
        case "Ranjeet":
            if password == 123:
                print(name, "You are allowed ")
            else:
                print(name, "You entered wrong password")
        case _:
            if name != "Ranjeet" or name != "Pramod":
                print(name, "You didn't registered for this Python class")


name = input("Enter your name = ")
password = int(input("Enter password to enter Python class = "))

allowed_to_attend_Python_class(name, password)