import numpy as np
import math


def hermitiana(mat):
    her = np.transpose(mat)
    # print(her)
    # print(mat)
    for i in range(len(her)):
        for j in range(len(her[i])):
            her[i][j] = complex(her[i][j])
    print(mat)
    her = her.conjugate()
    if mat == her:
        return True
    else:
        return False


def media(mat, ket):
    med = []
    for i in range(len(ket)):
        med.append(0)
    for j in range(len(mat)):
        for k in range(len(mat)):
            med[j] = mat[j][k] * ket[k]
    result = []
    for x in range(len(ket)):
        result.append(ket[x] * med[x])
    return result


def main():
    print('Ingrese los valores del vector Ket, separados por un espacio.')
    vec = input().split(" ")
    # print(vec)
    ket = []
    for i in vec:
        ket.append(complex(i))
    print('Ingrese las filas de la matriz, cuando termine ingrese una lista vacia')
    vec = input().split(" ")
    mat = []
    while vec != ['']:
        mat_1 = []
        for i in vec:
            mat_1.append(complex(i))
        mat.append(mat_1)
        vec = input().split(" ")
    R = hermitiana(mat)
    if R:
        print(media(mat, ket))
    else:
        print('La matriz es hermitiana.')


if __name__ == '__main__':
    main()
