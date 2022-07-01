import numpy as np

n = int(input('Numero de linhas\colunas: '))

matriz_a = []
#definido matriz A
print('Matriz A')
for l in range(0, n):
    linha = []
    for c in range(0, n):
        linha.append(int(input('X{}{}: '.format(l+1, c+1))))

    matriz_a.append(linha)

#definindo matriz B
matriz_b = []
print('Matriz B')
for l in range(0, n):
    linha = []
    for c in range(0, n):
        linha.append(int(input('X{}{}: '.format(l+1, c+1))))
    matriz_b.append(linha)

#encontrando valor escalar de x
lista_x = []
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            lista_x.append(matriz_a[i][j])

x = sum(lista_x)

#transposta de B
matriz_tb = []
for i in range(0, n):
    linha = []
    for j in range(0, n):
        linha.append(matriz_b[j][i])
    matriz_tb.append(linha)


#matriz R
#(x * A)
x_a = []
for i in range(0, n):
    linha = []
    for j in range(0, n):
        linha.append(x * matriz_a[i][j])
    x_a.append(linha)


matriz_r = np.dot(x_a, matriz_tb)
print('Matriz R:')
for i in range(0, n):
    for j in range(0, n):
        print(matriz_r[i][j], end = ' ')
    print()
