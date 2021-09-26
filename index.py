import random
from clear_screen import clear

caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lows = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
syms = ["!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

validChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
qwerty = ["`1234567890-=", "qwertyuip[]", "asdfghjkl;'#", "\\zxcvbnm,./"]

debug = False

# Generate combinations for QWERTY keyboard
combin = []
for i in qwerty:
    for x in range(len(i) - 2):
        combin.append(i[x:x+3])

def checkPassword(pw, firstname, lastname):
    clear()
    print("Checking password...")
    score = 0

    upper = False
    lower = False
    number = False
    symbol = False

    # Length check
    if len(pw) < 8 or len(pw) > 24:
        if debug:
            print("Too short or too long. Score is 0.")
        score = 0
        return score

    # Valid characters check
    if any(not i in validChars for i in pw):
        if debug:
            print("Invalid characters. Score is 0.")
        score = 0
        return score

    # Name check
    if firstname.lower() in pw.lower() or lastname.lower() in pw.lower():
        if debug:
            print("Contains first/last name. Score is 0.")
        score = 0
        return score

    # Length score
    score = score + len(pw)
    
    # Upper/lower/digits/symbols check
    if any(i.isupper() for i in pw):
        if debug:
            print("Uppercase. +5")
        score = score + 5
        upper = True
    if any(i.islower() for i in pw):
        if debug:
            print("Lowercase. +5")
        score = score + 5
        lower = True
    if any(i.isdigit() for i in pw):
        if debug:
            print("Digits. +5")
        score = score + 5
        number = True
    if any(i in syms for i in pw):
        if debug:
            print("Symbols. +5")
        score = score + 5
        symbol = True

    # Contains all or only one type check
    if upper and lower and number and symbol:
        if debug:
            print("All types. +10")
        score = score + 10
    if upper and lower and not number and not symbol:
        if debug:
            print("Only one type. -5")
        score = score - 5
    if not upper and not lower and number and not symbol:
        if debug:
            print("Only one type. -5")
        score = score - 5
    if not upper and not lower and not number and symbol:
        if debug:
            print("Only one type. -5")
        score = score - 5
    
    # Consecutive letter check
    for i in combin:
        if i in pw.lower():
            score = score - 5
            if debug:
                print("Found consecutive letters " + i + ". -5")

    return score

# Password generation
def genPassword(length):
    password = ""
    # Grab random number corresponding to set of characters, then grab random entry from list
    for x in range(0, length):
        num = random.randint(0, 3)
        if num == 0:
            password = password + random.choice(caps)
        if num == 1:
            password = password + random.choice(lows)
        if num == 2:
            password = password + random.choice(nums)
        if num == 3:
            password = password + random.choice(syms)
    return password

clear()
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")

while True:
    clear()
    print("Hi, " + firstname + "! Please choose an option.")
    print()
    print()
    print("1. Generate Password")
    print("2. Check Password")
    print("3. Exit")
    menu = int(input(": "))

    if menu == 1:
        clear()
        print("Password Generator")
        print()
        print()
        length = int(input("Please enter a password length: "))
        if length < 8 or length > 24:
            clear()
            print("Length too small or large.")
            print()
            print()
            input("Press enter to continue.")
        else:
            clear()
            print("Please wait, generating password...")

            pw = genPassword(length)
            check = checkPassword(pw, firstname, lastname)

            while check < 20:
                pw = genPassword(pw)
                check = checkPassword(pw, firstname, lastname)
            
            clear()
            print("Your generated password is:", pw)
            print("Score:", str(check))
            print()
            print()
            input("Press enter to continue.")

    if menu == 2:
        clear()
        print("Password Checker")
        print()
        print()

        pw = input("Please enter the password you would like to check: ")
        score = checkPassword(pw, firstname, lastname)

        if not debug:
            clear()

        if score > 0:
            print("Your password's score is", str(score))
            print()
            print()
            input("Press enter to continue.")
        else:
            print("This password is not sufficient or invalid (contains invalid characters).")
            print("Score: ", score)
            print()
            print()
            input("Press enter to continue.")

    elif menu == 3:
        print("Goodbye.")
        quit()
