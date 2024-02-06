from validation import validateRow, validate, asType





selection_operators = {
    '=': lambda a,b: a == b,
    '<=': lambda a,b: a <= b,
    '<': lambda a,b: a < b,
    '>=': lambda a,b: a >= b,
    '>': lambda a,b: a > b,
    '@': lambda a,b: b in a
}

class SelectOption:
    def __init__(self, operation, key, value):
        self.operation = operation
        self.key = key
        self.value = value

    def check(self, colnames, types, row):
        key_index = colnames.index(self.key)
        type = types[key_index]
        value_in_table = row[key_index]
        return self.operation(asType(value_in_table, type), asType(self.value, type))

def parseSelectQuery(raw):
    options = raw.replace(' ', '').split('\n')
    checks = []
    
    for option in options:
        possible_operation_keys = [key for key in selection_operators.keys() if key in option]
        if(len(possible_operation_keys) == 0):
            continue
        
        operation_key = possible_operation_keys[0]
        for candidate in possible_operation_keys:
            if(len(candidate) > len(operation_key)):
                operation_key = candidate
            
        key_value = option.split(operation_key)
        operation = selection_operators[operation_key]
        checks.append(SelectOption(operation, key_value[0], key_value[1]))
        
    return checks

assignment_operators = {
    '=': lambda a,b: b,
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b
}

class AssignOption:
    def __init__(self, operation, key, value):
        self.operation = operation
        self.key = key
        self.value = value

    def apply(self, colnames, types, row):
        key_index = colnames.index(self.key)
        type = types[key_index]
        value_in_table = row[key_index]
        if(not validate(self.value, type)):
            return
        result = self.operation(asType(value_in_table, type), asType(self.value, type))
        if(not validate(result, type)):
            return
        row[key_index] = result
        return row

def parseAssignQuery(raw):
    options = raw.replace(' ', '').split('\n')
    assignments = []

    for option in options:
        possible_operation_keys = [key for key in assignment_operators.keys() if key in option]
        if(len(possible_operation_keys) == 0):
            continue
        
        operation_key = possible_operation_keys[0]
        for candidate in possible_operation_keys:
            if(len(candidate) > len(operation_key)):
                operation_key = candidate
            
        key_value = option.split(operation_key)
        operation = assignment_operators[operation_key]
        assignments.append(AssignOption(operation, key_value[0], key_value[1]))

    return assignments


def parseInsertion(raw):
    options = [option for option in raw.replace(' ', '').split('\n') if (len(option) > 0)]
    return options


class Table:
    def __init__(self, colnames, types):
        self.colnames = colnames
        self.types = types
        self.rows = []
        
    def rename(self, colnames):
        self.colnames = colnames
        
    def select(self, options):
        results = []
        for row in self.rows:
            criteria_met = True
            for option in options:
                if(not option.check(self.colnames, self.types, row)):
                    criteria_met = False
                    break
            if(criteria_met):
                results.append(row)

        return results
    
    def delete(self, options):
        results = self.select(options)
        for result in results:
            self.rows.remove(result)

        return results

    def update(self, selection, assignments):
        selected = self.select(selection)
        for row in selected:
            for assignment in assignments:
                assignment.apply(self.colnames, self.types, row)

        return selected
                
        
    def insert(self, row):
        print(row)
        if(not validateRow(self, row)):
            return []
        self.rows.append(row)
        return row
