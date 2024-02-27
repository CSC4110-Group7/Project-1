from database import Table

#Global table
table = Table([""], ["string"])

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