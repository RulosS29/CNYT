from CNYT import *


def partes(n):
    a = n[0]
    b = n[1]
    return a, b


def sumavecomp(v, w):
    n = len(v)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = (v[k][0] + w[k][0], v[k][1] + w[k][1])
    return r


def inversoad(v):
    lon = len(v)
    r = [(0, 0)] * lon
    for x in range(lon):
        a_1, a_2 = partes(v[x])
        a_1 = a_1 * -1
        a_2 = a_2 * -1
        r[x] = (a_1, a_2)
    return r


def mulxc(v, c):
    lon = len(v)
    r = [(0, 0)] * lon
    for x in range(lon):
        a_1, a_2 = partes(v[x])
        r[x] = (a_1 * c, a_2 * c)
    return r


def sumatri(A, B):
    m = len(A)
    n = len(A[0])
    fila = [(0,0)] * n
    r = [fila]* m
    for j in range(m):
        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = (A[j][k][0]+B[j][k][0], A[j][k][1] + B[j][k][1])
    return r


def multimxc(A, c):
    m = len(A)
    n = len(A[0])
    fila = [(0,0)] * n
    r = [fila]* m
    for j in range(m):
        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = (c*(A[j][k][0]), c*(A[j][k][1]))
    return r


def transpuesta(A):
    m = len(A)
    n = len(A[0])
    fila = [(0,0)] * n
    r = [fila]* m
    for j in range(m):
        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            if k != j:
                res = A[j][k]
                r[j][k] = A[k][j]
                r[k][j] = res
            else:
                r[j][k] = A[j][k]
    return r


def adjunta(A):
    A = transpuesta(A)
    for j in range(len(A)):
        for k in range(len(A)):
            res = A[j][k][1]
            res = res*-1
            A[j][k] = A[j][k][0], res
    return A








