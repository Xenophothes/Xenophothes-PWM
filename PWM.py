import os, sys, random, string # os: os.system, os.listdir, os.path.isFile, os.path.join
# sys: sys.exit | random: random.randint | string: string.ascii[cases]
from time import sleep # time.sleep()

os.system("title Xenophothes")
os.system("color 09") # Console aesthetics
os.system("cls")

try:
    open("passwords/10010100101110101001010", 'r') # Check the password folder exists
except:
    try:
        os.makedirs("passwords") # Make passwords folder
    except:
        pass
    file = open("passwords/10010100101110101001010", 'w') # Create the first time texting file.
    file.close()

print("▒██   ██▒▓█████  ███▄    █  ▒█████   ██▓███   ██░ ██  ▒█████  ▄███████▓ ██░ ██ ▓█████   ██████ ")
print("▒▒ █ █ ▒░▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▓██░  ██▒▓██░ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▒██    ▒ ")
print("░░  █   ░▒███   ▓██  ▀█ ██▒▒██░  ██▒▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▒ ▓██░ ▒░▒██▀▀██░▒███   ░ ▓██▄   ")
print(" ░ █ █ ▒ ▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄   ▒   ██▒")
print("▒██▒ ▒██▒░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░  ▒██▒ ░ ░▓█▒░██▓░▒████▒▒██████▒▒") # Title
print("▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░▒ ▒▓▒ ▒ ░")
print("░░   ░▒ ░ ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░     ░     ▒ ░▒░ ░ ░ ░  ░░ ░▒  ░ ░")
print(" ░    ░     ░      ░   ░ ░ ░ ░ ░ ▒  ░░        ░  ░░ ░░ ░ ░ ▒    ░       ░  ░░ ░   ░   ░  ░  ░  ")
print(" ░    ░     ░  ░         ░     ░ ░            ░  ░  ░    ░ ░            ░  ░  ░   ░  ░      ░  ")

print("\nPassword Manager\n****************\n\n")
print("Save a new password")
print("Generate a new password")
print("Get a password")
print("Delete a password")
print("Show all passwords.")
print()
while True:
    try:
        i = input("> ").lower()
        i[0] + i[1] + i[2]
    except IndexError:
        print("Retry.")
        continue
    except Exception as e:
        print("Error: " + e)
        continue
    else:
        pass
    if (i == "save") or (i[0] == "save"): # Saving a new password.
        host = input("Host: ").lower()
        file = open("passwords/"+host, 'w')
        password = input("Password: ")
        file.write(password)
        file.close()
        print("Done.\n")
    elif (i[0] == 'g') and (i[2] == 'n'): # Generating a password to use.
        characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        passwordLength = 12
        password = ""
        for i in range(passwordLength):
            password += characters[random.randint(0, len(characters)-1)]
        print("Generated Password: " + str(password))
    elif (i[0] == 'g') and (i[2] == 't'): # Retreiving a password from the database.
        while True:
            passFor = input("Please enter the password for: ").lower()
            hosts = [f for f in os.listdir("passwords") if os.path.isfile(os.path.join("passwords", f))]
            if (passFor in hosts):
                password = open("passwords/"+passFor, 'r').read()
                print("Password: '" + password + '\'')
                print()
                break
            else:
                print("No password for that.")
                print()
                break
    elif (i == "delete") or (i[0] == 'd'): # Deleting a password from the database
        hosts = [f for f in os.listdir("passwords") if os.path.isfile(os.path.join("passwords", f))]
        host = input("Host: ").lower()
        if (host in hosts):
            os.remove("passwords/"+host)
            print("Removed.")
            print()
            continue
        else:
            print("That host does not exist.")
            print()
            continue
    elif (i == "show") or (i[0] == "show"): # Showing all the passwords in the database.
        hosts = [f for f in os.listdir("passwords") if os.path.isfile(os.path.join("passwords", f))]
        for host in hosts:
            if (host == "10010100101110101001010") or (host == "desktop.ini"):
                continue
            else:
                password = open("passwords/"+str(host), 'r').read()
                print("'" + host + "': '" + password + '\'')
    else:
        print("Retry.")
        continue
                                                                                               

