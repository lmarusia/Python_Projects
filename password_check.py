def check(password):
    strength = 0 #password strength
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # List of numbers
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~'] # List of special characters

    #Checks Password length (minimum 8 char recomended)
    if len(password) > 8:
        strength += 1

    #Checks for lowercase letters
    if not any(char.islower() for char in password):
        pass
    else:
        strength += 1

    #Checks for uppercase letters
    if not any(char.isupper() for char in password):
        pass
    else:
        strength += 1

    #Checks for special characters
    if not any(char in special_characters for char in password):
        pass
    else:
        strength += 1

    #Checks for numbers
    if not any(char in numbers for char in password):
        pass
    else:
        strength += 1

    #Less than 3 of the parameters were met - Weak Password
    if strength < 3:
        print("Weak Password")
        print("Strength: " + str(strength))
        print("***************")

    #More than 3 of the parameters were met - Strong Password
    if strength > 3:
        print("Strong Password")
        print("Strength: " + str(strength))
        print("***************")

user = input("Enter password to check: ")
check(user)