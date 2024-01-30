

#Global csv data
columnNames = []
data = [[]]



def readCsv(file):
    global columnNames
    global data

    columnNames.clear()
    data.clear()

    names = file.readline()
    for name in names.split(','):
        columnNames.append(name.strip())

    for line in file:
        data.append(line.strip().split(','))

    file.close()

def saveCsv(file):
    global columnNames
    global data

    namesOut = ""
    for name in columnNames:
        namesOut += name + ','
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