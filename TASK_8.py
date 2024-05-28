#Level 2 Task 3

def checkPassword(password):
    upperCharacters, lowerCharacters, specialCharacters,digits,length = 0, 0, 0, 0, 0
    length = len(password)

    if (length < 6):
        print("Password must be at least 6 characters\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperCharacters += 1
            elif (password[i].islower()):
                lowerCharacters += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialCharacters += 1

    if (upperCharacters != 0 and lowerCharacters != 0 and digits != 0 and specialCharacters != 0):
        if (length >= 10):
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is Poor.\n")
    else:
        if (upperCharacters == 0):
            print("Password must contain at least one uppercase character!\n")
        if (lowerCharacters == 0):
            print("Password must contain at least one lowercase character!\n")
        if (specialCharacters == 0):
            print("Password must contain at least one special character!\n")
        if (digits == 0):
            print("Password must contain at least one digit!\n")


password = input("Please enter password: ")
checkPassword(password)
