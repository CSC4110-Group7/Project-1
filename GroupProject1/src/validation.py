import re
import tkinter as tk


# email_pattern = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', re.IGNORECASE)
email_pattern = re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', re.IGNORECASE)
phone_pattern = re.compile(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
ssn_pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
# phone_pattern = re.compile(r'^\+?1?\d{9,15}$')


def validateRow(table, row):
    if(len(row) != len(table.colnames)):
        return False

    for i, value in enumerate(row):
        if(not validate(value, table.types[i])):
            return False
    return True

def validate(value, type):
    valid = True

    if type == 'email':
        valid = email_pattern.match(value)
    elif type == 'ssn':
        valid = ssn_pattern.match(value)
    elif type == 'phone':
        valid = phone_pattern.match(value)
    elif type == 'alpha':
        valid = str(value).isalpha()
    elif type == 'alphanum':
        valid = str(value).isalnum()
    elif type == 'int':
        try:
            int(value)
            valid = True
        except:
            valid = False
    elif type == 'float':
        try:
            float(value)
            valid = True
        except:
            valid = False
    elif type == 'string':
        valid = len(value) > 0
    # Add more validations as needed
        
    if(not valid):
        tk.messagebox.showerror(title="Invalid Entry", message=f'Expected value of {type} but received: {value}')
    return valid



def asType(value, type):
    match type:
        case 'email','ssn','phone','alpha','alphanum','string':
            return str(value)
        case 'int':
            return int(value)
        case 'float', 'number':
            return float(value)
        case _:
            return str(value)