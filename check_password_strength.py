import string
def check_password_strength(password):
    if(10<len(password)>15):
        return "Weak:Password should be minimum 10 characters and maximum 15 characters"
    elif(not any(char.isupper()for char in password)or not any(char.islower()for char in password) or not any(char.isdigit()for char in password) or not any(char in string.punctuation for char in password)):
        return "Weak:Password should contain atleast 1 uppercase letter,1 lowercase letter,1 digit and 1 special character "
    elif any(char.isspace() for char in password):
        return "Password should not contain white spaces"
    elif password[-1]=='.' or password[-1]=='@':
        return "Password should not end with dot and @"
    else:
        return "Strong password"
password=input("Enter the password")
print(check_password_strength(password))