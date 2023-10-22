import math


def prime(nombre):
    if (nombre == 1):
        return False
    for i in range(2, (int)(math.sqrt(nombre) + 1)):
        frac = (nombre / i)
        entier = int(frac)
        if frac == entier:
            return False
    return True


def goldbach(nombre):
    for i in range(1, nombre):
        if prime(i) and prime(nombre - i):
            print(nombre, " :", i, " + ", nombre - i)
            return True
    print("no results found")
    return False

def is_goldbach_conjecture_true():
    nombre = 4
    while goldbach(nombre):
        nombre += 2
    return False

is_goldbach_conjecture_true()

