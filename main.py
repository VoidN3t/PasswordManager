# This script is a simple password manager that allows users to add, delete, and view entries with associated passwords.
#Developers: @VoidN3t [Copilot (Most of the code)]
#Discord: voidn3t_fake




# Importing the necessary libraries
import pyperclip as pc
# Initializing the necessary variables
entries = []
entriesPassword = []
# Printing the welcome message and instructions for the user
print("""
--Password Manager--
Developers: @VoidN3t [Copilot (That just became pilot)]
Firt thing first, set a universal password
This password will be used to access the entries
Type /setUniversalPassword to set the universal password
Type /help for a list of commands
Type /exit to exit the program
""")

# This is the main loop of the program that will run indefinitely until the user exits
while True:
    # This function will analyze the user input and perform actions based on it
    # It will check for specific commands and print corresponding messages
    def promtAnalisys(userPromt):
        if userPromt == "/setUniversalPassword":
            global universalPassword  # Declare universalPassword as global to modify it
            universalPassword = ""
            if universalPassword != "":
                print("Universal password already set")
            inputNewPassword = input("New password: ")
            inputConfirmPassword = input("Confirm password: ")
            if inputNewPassword != inputConfirmPassword:
                print("Passwords do not match")
                return
            universalPassword = inputNewPassword
            print("Universal password set")
        elif userPromt == "/exit":
            print("Bye")
            exit()
        elif userPromt == "/help":
            print("Commands: /help, /exit, /entryAdd, /entryDelete, /entry, /reset, /setUniversalPassword")
        elif userPromt == "/entry":
            entryName = input("Entry Name: ")
            if entryName in entries:
                print("Entry found")
                index = entries.index(entryName)
                inputPassword = input("Password: ")
                if inputPassword != universalPassword:
                    print("Invalid password")
                    return
                print("Password is correct")
                pc.copy(entriesPassword[index])
                print(f"Entry '{entryName}' found")
            else:
                print(f"Entry '{entryName}' not found")
        elif userPromt == "/entryDelete":
            entryName = input("Entry Name: ")
            if entryName in entries:
                index = entries.index(entryName)
                inputPassword = input("Password: ")
                if inputPassword != universalPassword:
                    print("Invalid password")
                    return
                print("Password is correct")
                print("Entry found")
                del entries[index]
                del entriesPassword[index]
                print(f"Entry '{entryName}' deleted")
            else:
                print(f"Entry '{entryName}' not found")
        elif userPromt == "":
            print("Empty input")
        elif userPromt == "/entryAdd":
            entryName = input("Entry Name: ")
            entries.append(entryName)
            entryPassword = input("Password to save in the entry: ")
            entriesPassword.append(entryPassword)
            print(f"Entry '{entryName}' saved and registered password '{entryPassword}'")
        elif userPromt == "/reset":
            inputPassword = input("Password: ")
            if inputPassword != universalPassword:
                print("Invalid password")
                return
            print("Password is correct")
            print("Entries reset")
            entries.clear()
            entriesPassword.clear()
            print("Universal password reset")
            universalPassword = ""    
        else:
            print("Unknown command")
    # This function will prompt the user for input and call the promtAnalisys function with the input
    # It will continue to prompt the user until a valid command is entered
    promt = input("> ")
    # Call the promtAnalisys function with the user input
    promtAnalisys(promt)