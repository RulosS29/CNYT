from sys import stdin


def main():
    mat_f = []
    print('Ingrese la matriz de 0 y 1 Correspondientes, cuando termine de escribirla, ingrese una linea vacía.')
    mat = list(map(int, stdin.readline().strip().split()))
    while mat:
        # print(mat)
        mat_f.append(mat)
        mat = list(map(int, stdin.readline().strip().split()))
    print(mat_f)

    print('Ingrese el estado inicial')
    v_ini = list(map(int, stdin.readline().strip().split()))
    print(v_ini)
    print('Numero de clicks')
    clicks = int(stdin.readline().strip())
    C = []
    for k in range(clicks):
        C_1 = []
        for i in range(len(v_ini)):
            ans = 0
            for j in range(len(v_ini)):
                print(j)
                ans += mat_f[i][j] * v_ini[j]
            C_1.append(ans)
        C = C_1
    print(C)


if __name__ == '__main__':
    main()
