import math


def suma(com_1, com_2):
    a_1, b_1 = com_1.real, com_1.imag
    a_2, b_2 = com_2.real, com_2.imag

    a, b = a_1+a_2, b_1+b_2
    return complex(a, b)


def producto(com_1, com_2):
    if com_1 == 0 or com_2 == 0:
        return 0
    else:
        a_1, b_1 = com_1.real, com_1.imag
        a_2, b_2 = com_2.real, com_2.imag

        a, b = a_1 * a_2 - b_1*b_2, a_1*b_2 + a_2*b_1
        return complex(a, b)


def resta(com_1, com_2):
    a_1, b_1 = com_1.real, com_1.imag
    a_2, b_2 = com_2.real, com_2.imag

    a, b = a_1 - a_2, b_1 - b_2
    if complex(a, b) == 0:
        return 0
    else:
        return complex(a, b)


def division(com_1, com_2):
    if com_1 == 0 or com_2 == 0:
        return "No es posible"
    else:
        a_1, b_1 = com_1.real, com_1.imag
        a_2, b_2 = com_2.real, com_2.imag

        a, b = (a_1*a_2 + b_1*b_2)/(a_2**2+b_2**2), (a_2*b_1 - a_1*b_2)/(a_2**2+b_2**2)
        return complex(a, b)


def modulo(com_1):
    a_1, b_1 = com_1.real, com_1.imag

    return math.sqrt(a_1**2 + b_1**2)


def conjugado(com_1):
    a_1, b_1 = com_1.real, com_1.imag

    return complex(a_1, b_1*-1)


def conversionp(com_1):
    a_1, b_1 = com_1.real, com_1.imag
    if a_1 == 0:
        return 0, 0
    else:
        p = modulo(com_1)
        teta = math.atan(b_1/a_1)
        return p, teta


def conversionc(p, teta):
    teta = math.degrees(teta)
    a = p*math.cos(teta)
    b = p*math.sin(teta)

    return complex(a, b)


def retonar(com_1):
    a_1, b_1 = com_1.real, com_1.imag
    if a_1 == 0:
        return "No es posible"
    else:
        return math.atan(b_1/a_1)
