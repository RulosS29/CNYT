def tran(ket):
    ans = 0
    for k in range(len(ket)):
        # print(ket[k].imag)
        ans += (ket[k].real**2+ket[k].imag**2)
    ans = 1/ans
    for k in range(len(ket)):
        ket[k] = ket[k]*ans
    result = []
    for k in range(len(ket)):
        # print(ket[k])
        bra = ket[k].conjugate()
        # print(bra)
        result.append(ket[k]*bra)
    return result


def main():
    print('Ingrese los valores del vector Ket, separados por un espacio.')
    vec = input().split(" ")
    # print(vec)
    ket = []
    for i in vec:
        ket.append(complex(i))
    # print(ket)
    # print(ket[0])
    print(tran(ket))


if __name__ == '__main__':
    main()
