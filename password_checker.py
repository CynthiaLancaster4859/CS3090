import re
import getpass

def password_strength(password):

    #check length of password 
    if len(password) < 8:
        return "WEAK: Your password is less than 8 characters long"

    #check for uppercase letter 
    if not re.search(r'[A-Z]', password):
        return "OKAY: Your password doesn't have a Captial letter"
    
    #check for a number
    if not re.search(r'[0-9]', password):
        return "OKAY: Your password doesn't have a number"
    
    #check for special character
    if not re.search(r'[@!%*?&]', password):
        return "OKAY: Your password doesn't have a special character"
    
    return "STRONG: Your password is really strong!"

user_password = getpass.getpass("Enter a password. Lets see how strong it is 💪: ")
print(password_strength(user_password))