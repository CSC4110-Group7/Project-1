import re
from database import Table

#Global table
table = Table([""], ["string"])

email_pattern = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', re.IGNORECASE)
ssn_pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
phone_pattern = re.compile(r'^\+?1?\d{9,15}$')

def readCsv(file):
    global table
    
    table.colnames.clear()
    table.types.clear()
    table.rows.clear()

    names = file.readline()
    for name in names.strip().split(','):
        nsplit = name.split('.')
        table.colnames.append(nsplit[0])

        if(len(nsplit) > 1):
            table.types.append(nsplit[1])
        else:
            table.types.append('string')

    for line in file:
        row = line.strip().split(',')
        if(len(row) != len(table.colnames)):
            continue
        table.rows.append(row)

    file.close()
    
    return table

def saveCsv(file):
    global table
    
    namesOut = ",".join([f"{col}.{typ}" for col, typ in zip(table.colnames, table.types)]) + '\n'
    file.write(namesOut)

    for row in table.rows:
        rowOut = ','.join([value for value in row]) + '\n'
        file.write(rowOut)

    file.close()

def validateData(row):
    for i, value in enumerate(row):
        if i >= len(table.types):  # Prevent index out of range if row has more values than expected
            return False
        type = table.types[i]
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

def deleteData(uniqueId):
    global table
    data = [row for row in data if row[0] != uniqueId]




#
#   Store loaded csv as...
#   in class?
#   columnNames[]
#   data[]
#