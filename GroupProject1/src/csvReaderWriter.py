import re

#Global csv data
columnNames = []
types = []
data = [[]]

email_pattern = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', re.IGNORECASE)
ssn_pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
phone_pattern = re.compile(r'^\+?1?\d{9,15}$')

def readCsv(file):
    global columnNames, data, types

    columnNames.clear()
    data.clear()
    types.clear()

    names = file.readline()
    for name in names.strip().split(','):
        nsplit = name.split('.')
        columnNames.append(nsplit[0])

        if(len(nsplit) > 1):
            types.append(nsplit[1])
        else:
            types.append('string')

    for line in file:
        data.append(line.strip().split(','))

    file.close()

def saveCsv(file):
    global columnNames, data, types

    namesOut = ",".join([f"{col}.{typ}" for col, typ in zip(columnNames, types)]) + '\n'
    file.write(namesOut)

    for row in data:
        rowOut = ""
        for value in row:
            rowOut += value + ','
        rowOut = rowOut.removesuffix(',') + '\n'
        file.write(rowOut)

    file.close()

def validateData(row):
    for i, value in enumerate(row):
        if i >= len(types):  # Prevent index out of range if row has more values than expected
            return False
        type = types[i]
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
    global data

    data = [row for row in data if row[0] != uniqueId]




#
#   Store loaded csv as...
#   in class?
#   columnNames[]
#   data[]
#