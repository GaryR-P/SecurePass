# Must be 12 characters or more
# At least one uppercase, lowercase, digit, and special symbol
# No obvious patterns ...qwert 1234...

input_password = input("Enter a password: ")

def check_password(password):
    if len(password) < 12:
        print("Password must be 12 characters in length or more")
        return False

    for char in password:
        if char.isupper():
            break
        else:
            if char == password[len(password)-1]:
                print("Password must contain at least one uppercase letter")
                return False

    for char in password:
        if char.islower():
            break
        else:
            if char == password[len(password)-1]:
                print("Password must contain at least one lowercase letter")
                return False

    for char in password:
        if char.isdigit():
            break
        else:
            if char == password[len(password)-1]:
                print("Password must contain at least one digit")
                return False

    for char in password:
        if char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']:
            break
        else:
            if char == password[len(password)-1]:
                print("Password must contain at least one special symbol")
                return False

    if not patterns_checker(password):
        return False

    return True

def patterns_checker(password):
    keyboardorder = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']

    for i in range(len(password)-2):
        if password[i] == password[i+1] and password[i] == password[i+2]:
            print("Password must not contain three characters in a row")
            return False

        if password[i].isdigit() and password[i+1].isdigit() and password[i+2].isdigit():
            if int(password[i]) + 1 == int(password[i+1]) and int(password[i+1]) + 1 == int(password[i+2]):
                print("Password must not contain three numbers in a row")
                return False
            if int(password[i]) - 1 == int(password[i+1]) and int(password[i+1]) - 1 == int(password[i+2]):
                print("Password must not contain three numbers in a row")
                return False

        if password[i] in keyboardorder and password[i+1] in keyboardorder and password[i+2] in keyboardorder:
            if keyboardorder.index(password[i]) + 1 == keyboardorder.index(password[i+1]) and keyboardorder.index(password[i+1]) + 1 == keyboardorder.index(password[i+2]):
                print("Password must not contain three letters in a row")
                return False
            if keyboardorder.index(password[i]) - 1 == keyboardorder.index(password[i+1]) and keyboardorder.index(password[i+1]) - 1 == keyboardorder.index(password[i+2]):
                print("Password must not contain three letters in a row")
                return False

    return True


