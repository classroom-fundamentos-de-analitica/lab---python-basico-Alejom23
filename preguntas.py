"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import os


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row[0:-1] for row in data]
    data = [row.split() for row in data]
    data = [row[1] for row in data]
    suma = 0
    for row in data:
        suma += int(row)
    return suma
#print(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row[0:-1] for row in data]
    data = [row.split() for row in data]
    data = [row[0] for row in data]
    letras = set(data)
    conteo = {}
    resultado = []
    for letra in letras:
        conteo[letra] = 0
    for row in data:
        conteo[row] += 1
    
    for key, value in conteo.items():
        resultado.append((key, value))
    resultado = sorted(resultado)
    return resultado

#print(pregunta_02())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row[0:-1] for row in data]
    data = [row.split() for row in data]
    data = [[row[0], row[1]] for row in data]
    columna_letras = [row[0] for row in data]
    letras = set(columna_letras)
    conteo = {}
    resultado = []
    for letra in letras:
        conteo[letra] = 0
    for row in data:
        conteo[row[0]] += int(row[1])
    
    for key, value in conteo.items():
        resultado.append((key, value))
    resultado = sorted(resultado)
    return resultado

#print(pregunta_03())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [row[2].split("-")[1] for row in data]
    meses = set(data)
    conteo = {}
    resultado = []
    for mes in meses:
        conteo[mes] = 0
    for row in data:
        conteo[row] += 1
    
    for key, value in conteo.items():
        resultado.append((key, value))
    resultado = sorted(resultado)
    return resultado

#print(pregunta_04())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [[row[0], row[1]] for row in data]

    letters = {}
    for row in data:
        letter = row[0]
        quant = int(row[1])
        if letter not in letters:
            letters[letter] = {"min" : quant,
                                "max":quant}
        else:
            if quant > letters[letter]["max"]:
                letters[letter]["max"] = quant
            elif quant < letters[letter]["min"]:
                letters[letter]["min"] = quant

    result = []
    for letter in letters:
        result.append((letter, letters[letter]["max"], letters[letter]["min"]))

    result = sorted(result, key= lambda x:x[0])

    return result

#print(pregunta_05())
    



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [row[4].split(",") for row in data]

    letters = {}
    for row in data:
        for code in row:
            letter = code.split(":")[0]
            quant = int(code.split(":")[1])
            if letter not in letters:
                letters[letter] = {"min" : quant,
                                    "max":quant}
            else:
                if quant > letters[letter]["max"]:
                    letters[letter]["max"] = quant
                elif quant < letters[letter]["min"]:
                    letters[letter]["min"] = quant

    result = []
    for letter in letters:
        result.append((letter, letters[letter]["min"], letters[letter]["max"]))

    result = sorted(result, key= lambda x:x[0])

    return result
    
#print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [[row[0], row[1]] for row in data]

    numbers = {}
    for row in data:
        number = row[1]
        letter = row[0]
        if number not in numbers:
            numbers[number] = []
        numbers[number].append(letter)

    result = []
    for number in numbers:
        result.append((int(number), numbers[number]))

    result = sorted(result, key= lambda x:x[0])

    return result

#print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [[row[0], row[1]] for row in data]

    numbers = {}
    for row in data:
        number = row[1]
        letter = row[0]
        if number not in numbers:
            numbers[number] = []
        numbers[number].append(letter)

    result = []
    for number in numbers:
        result.append((int(number), sorted(list(set(numbers[number])))))

    result = sorted(result, key= lambda x:x[0])

    return result

#print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [row[4].split(",") for row in data]

    letters = {}
    for row in data:
        for code in row:
            letter = code.split(":")[0]
            quant = int(code.split(":")[1])
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

    result = {}
    for key in sorted(letters):
        result[key] = letters[key]

    return result

#print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [[row[0], row[3], row[4]] for row in data]

    letters = []
    for row in data:
        letters.append((row[0], len(row[1].split(",")), len(row[2].split(","))))

    return letters

#print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [[row[1], row[3]] for row in data]

    letters_dict = {}
    for row in data:
        letters = row[1].split(",")
        number = int(row[0])
        for letter in letters:
            if letter not in letters_dict:
                letters_dict[letter] = number
            else:
                letters_dict[letter] += number

    result = {}
    for key in sorted(letters_dict):
        result[key] = letters_dict[key]

    return result

#print(pregunta_11())

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    script_dir = os.path.dirname(__file__) + "/data.csv"
    #print(script_dir)
    data = open(script_dir, 'r').readlines()
    data = [row for row in data]
    data = [row.split() for row in data]
    data = [[row[0], row[4]] for row in data]

    letters = {}
    for row in data:
        letter = row[0]
        numbers = [int(x.split(":")[1]) for x in row[1].split(",")]
        for number in numbers:
            if letter not in letters:
                letters[letter] = number
            else:
                letters[letter] += number

    result = {}
    for key in sorted(letters):
        result[key] = letters[key]

    return result


#print(pregunta_12())