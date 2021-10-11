from sys import stdin


def prob_vec(Ket, prob):
    # print('Probabilidad')
    ans = 0
    # print(Ket)
    for k in range(len(Ket)):
        # print(Ket[k])
        ans += (Ket[k].real**2+Ket[k].imag**2)
    return ((Ket[prob].real**2+Ket[prob].imag**2)/ans)


def main():
    print('Ingrese los valores del vector Ket, separados por un espacio.')
    vec = input().split(" ")
    # print(vec)
    ket = []
    for i in vec:
        ket.append(complex(i))
    print(ket)
    # print(ket[0])
    print('Ingrese la posicion el cual desea saber la probabilidad')
    prob = int(stdin.readline().strip())
    print(prob_vec(ket, prob))


if __name__ == '__main__':
    main()