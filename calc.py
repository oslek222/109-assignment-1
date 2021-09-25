# description

# imports
from display import print_menu, print_header
# global

# functions


# direct instructions
print_header()
print_menu()

option = input("select an option: ")

num1 = float(input("provide num1: "))
num2 = float(input("provide num2: "))


if(option == "1"):
    res = num1 + num2


elif(option == "2"):
    res = num1 - num2


elif(option == "3"):
    res = num1 * num2
    print(f"result: {res}")

elif(option == "4"):
    if not num2 == 0
    if(num2 == 0):
        print("error: nope!")
        res = "nope!"

    print(f"result: {res}")
