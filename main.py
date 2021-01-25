###Emanuel###

#Importing things.
import sys
import os
import time

#Function that clears the terminal/console.
def clear():
    os.system('cls||clear')

#Clearing the terminal.
clear()

#Opening message. This is the first line the user will see.
print("Welcome!\n")

#Asking the user for input.
text = input("Please enter the word \"continue\" to continue: ")

#If the user entered the word "continue" the program will continue. If not. The user will be prompted to state it again.
#This is an endless loop unless the user actually enters the correct input which is "continue".
if text == "continue" or text == "Continue":
    clear()
else:
    while True:
        text = input("Please enter the word \"continue\" to continue: ")
        if text == "continue" or text == "Continue":
            break
        else:
            pass

#Clearing the terminal.
clear()

#This part simply explains what the program does. The user will once again have to enter the word "continue" to go on.
print("The purpose of this program is to read a string provided by the user and then announce if the first and last characters are the same or not.\n")

text = input("Please enter the word \"continue\" to continue: ")

if text == "continue" or text == "Continue":
    clear()
else:
    while True:
        text = input("Please enter the word \"continue\" to continue: ")
        if text == "continue" or text == "Continue":
            break
        else:
            pass

#Clearing the terminal.
clear()


#The main loop that goes on forever.
while True:
    #Taking input from user.
    text = input("Enter a string that you would like me to analyze: ")

    #Checking what the first and last characters are.
    value_1 = text[0]
    value_2 = text[-1]

    #Checking if first and last characters in the string are the same.
    if value_1 == value_2:
        print("\nThe first character is the same as the last character!")
    else:
        print("\nThe first and last characters are not the same...")

    #Asking the user to enter the word "again". If he/she does the loop will just repeat. The user can also say "exit" to exit the program.
    print("\nEnter the word \"again\" if you want to analyze another string.")
    print("\nEnter the word \"exit\" in order to exit the program.")
    text = input("\nWhat do you want to do?: ")

    if text == "exit" or text == "Exit":
        sys.exit()
    if text == "again" or text == "Again":
        clear()
    else:
        while True:
            print("\nEnter the word \"again\" if you want to analyze another string.")
            print("\nEnter the word \"exit\" in order to exit the program.")
            text = input("\nWhat do you want to do?: ")
            if text == "again" or text == "Again":
                break
            else:
                if text == "exit" or text == "Exit":
                    sys.exit()
    clear()