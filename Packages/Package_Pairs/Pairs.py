def multiply_sets(A: list,B: list) -> list:
    C = []
    for a in A:
        for b in B:
            result = [a,b]
            C.append(result)
    return C

def relationship(A: list,B: list, equation: str) -> list:
    C = []

    for a in A:
        for b in B:
            x = int(a)
            y = int(b)
            safe_dict = {'x' : x, 'y' : y}
            if eval(equation, {"__builtins__": None}, safe_dict):
                C.append([a, b])

    return C

def relationship_matrix(A: list, B:list, AxB: list, C: list) -> list:
    """Makes a matrix to check values from 2 sets

    Args:
        A (list): First set. It's used to build the matrix's rows
        B (list): Second set. It's used to build the matrix's colums
        AxB (list): Product between A and B
        C (list): Relationship between A and B

    Returns:
        list: A matrix with A values as rows and B values as colums. Matrix[i][j] has 0 or 1 value if the relationship is false or true.
    """
    D = [[0] * len(B) for _ in range(len(A))]
    row = 0
    column = 0
    j = 0

    for pair in AxB:
        if column == len(B):
            column = 0
            row += 1
        if j < len(C) and pair == C[j]:
            D[row][column] = 1
            j += 1
        column += 1

    return D

def show_array(array: list):
    """ Recieves an array and prints a formatted version of it.

    Args:
        array (list): The array you want to print.

    """
    message = "[ "
    for i in range(len(array)):
        for j in range(len(array[i])):
            message += f"{array[i][j]} "
        if i == len(array) - 1:
            message += "]"
        else:
            message += "\n  "
    return message

def get_domain(C: list) -> set:
    domain = {pair[0] for pair in C}
    return domain

def get_range(C: list) -> set:
    range = {pair[1] for pair in C}
    return range

def relation_properties(A: list, C: list) -> str:
    message = []
    message.append(reflexive_property(A,C))
    message.append(symmetric_property(C))
    message.append(symmetric_property(C))
    message.append(transitive_property(C))
    message = " | ".join(message)
    return message


def reflexive_property(A: list,B: list) -> str:
    reflexives = []
    message = ""
    for i in range(len(A)):
        if [A[i], A[i]] in B:
            reflexives.append([A[i],A[i]])
    if len(reflexives) == len(A):
        message = "Reflexiva"
    elif len(reflexives) > 0:
        message = "No reflexiva"
    else:
        message = "Areflexiva"
    return message

def symmetric_property(C: list) -> str:
    is_symmetric = True
    has_symmetric = False
    is_antisymmetric = True
    
    for a, b in C:
        if [b, a] not in C and is_symmetric:
            is_symmetric = False
        elif [b,a] in C and has_symmetric == False:
            has_symmetric = True
        if a != b and [b, a] in C:
            is_antisymmetric = False
    
    if is_symmetric:
        return "Simétrica"
    elif is_antisymmetric:
        return "Antisimétrica"
    elif has_symmetric:
        return "Asimétrica"
    else:
        return "No simétrica"

def transitive_property(C: list) -> str:
    has_transitive = False
    is_transitive = True
    for x in C:
        for y in C:
            if x[1] == y[0]:
                if [x[0], y[1]] not in C:
                    is_transitive = False
                else:
                    has_transitive = True
    message = ""
    if is_transitive:
        message = "Transitiva"
    elif has_transitive:
        message = "No transitiva"
    else:
        message = "Atransitiva"
    return message

def relationship_clasify(properties: str,A: list, C: list) -> str:
    message = ''
    if 'Transitiva' in properties:
        if 'Reflexiva' in properties and 'Simétrica' in properties:
            message = 'Relación de equivalencia'
        elif 'Reflexiva' in properties and 'Antisimétrica' in properties:
            message = 'Relación de orden amplio'
        elif 'Arreflexiva' in properties and 'Asimétrica' in properties:
            message = 'Relación de orden estricto'
    if 'Relación de orden' in message:
        if len(A) * len(A) == len(C):
            message += ' total'
        else:
            message += ' parcial'
    return message