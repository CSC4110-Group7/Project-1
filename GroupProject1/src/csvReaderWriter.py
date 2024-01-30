

#Global csv data
columnNames = []
types = []
data = [[]]


def readCsv(file):
    global columnNames
    global data
    global types

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
    global columnNames
    global data
    global types

    namesOut = ""
    for i in range(len(columnNames)):
        namesOut += columnNames[i] + '.' + types[i] + ','
    namesOut = namesOut.removesuffix(',') + '\n'

    file.write(namesOut)

    for row in data:
        rowOut = ""
        for value in row:
            rowOut += value + ','
        rowOut = rowOut.removesuffix(',') + '\n'
        file.write(rowOut)

    file.close()




#
#   Store loaded csv as...
#   in class?
#   columnNames[]
#   data[]
#