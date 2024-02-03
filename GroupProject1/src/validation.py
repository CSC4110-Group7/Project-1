import re


email_pattern = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', re.IGNORECASE)
ssn_pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
phone_pattern = re.compile(r'^\+?1?\d{9,15}$')


def validateRow(table, row):
    if(len(row) != len(table.colnames)):
        return False

    for i, value in enumerate(row):
        if(not validate(value, table.types[i])):
            return False
    return True

def validate(value, type):
    if type == 'email':
        return email_pattern.match(value)
    elif type == 'ssn':
        return ssn_pattern.match(value)
    elif type == 'phone':
        return phone_pattern.match(value)
    elif type == 'alpha':
        return str(value).isalpha()
    elif type == 'alphanum':
        return str(value).isalnum()
    elif type == 'int':
        return str(value).isdigit()
    elif type == 'float':
        return str(value).isnumeric()
    elif type == 'string':
        return len(value) > 0
    # Add more validations as needed
    return True



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