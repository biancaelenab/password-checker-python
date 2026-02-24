import re

def check_password(password):
    errors = []

    if len(password) < 10:
        errors.append("Password must be at least 10 characters long!")

    if not re.search(r"[A-Z]",password):
        errors.append("Password must contain at least one upper case letter!")
    
    if not re.search(r"[0-9]",password):
        errors.append("Password must contain at least one number!")
    
    if not re.search(r"[!@#$%^&*()?/\\]", password):
        errors.append("Password must contaain at least one special character!")

    return errors

