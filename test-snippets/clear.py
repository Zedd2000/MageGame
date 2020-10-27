# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

input("enter some text to clear the screen and move to screen 2")

# now call function we defined above
clear()

input("Welcome to screen 2")
