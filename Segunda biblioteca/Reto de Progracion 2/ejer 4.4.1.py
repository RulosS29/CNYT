import numpy as np
import math


def multi(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[i].append(0)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k]*B[k][j]
    return result


def unitary(A, B):
    print('Unitaria')
    A_T = np.transpose(A)
    B_T = np.transpose(B)
    A_T = A_T.conjugate()
    B_T = B_T.conjugate()
    print(A,  'A original')
    print(A_T, 'A dagita')
    A_1 = multi(A, A_T)
    B_1 = multi(B, B_T)
    for j in range(len(B_1)):
        for k in range(len(B_1[0])):
            B_1[j][k] = int(B_1[j][k])
    iden = [[1,0],[0,1]]
    print(A_1, B_1)
    if A_1 == iden and B_1 == iden:
        return True
    else:
        return False


def main():
    A = [[0,1],[1,0]]
    B = [[math.sqrt(2)/2, math.sqrt(2)/2], [math.sqrt(2)/2, -math.sqrt(2)/2]]
    result = unitary(A, B)
    if result:
        res = multi(A, B)
        res_1 = np.transpose(res)
        res_1 = res_1.conjugate()
        result = multi(res, res_1)
        for j in range(len(result)):
            for k in range(len(result[0])):
                result[j][k] = int(result[j][k])

        print(result)
        if result == [[1,0],[0,1]]:
            print(True)
        else:
            print(False)
    else:
        print(False)


if __name__ == '__main__':
    main()
