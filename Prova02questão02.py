import numpy as np
def referenciaAutor():
    n = str(input('digite seu nome: ')).strip()
    nome = n.split(' ')
    n2 = len(nome) - 1
    nome2 = nome[-1]
    n3 = n.title()
    nome.remove(nome2)
    nome3 = ' '.join(nome)
    print(nome2.upper(),',',nome3[0:len(nome3)-1].title() )

referenciaAutor()
def matrizt():
    
    matriz_n = []
    for i in range(0, m):
        for j in range(0, n):
            matriz_n.append(matriz[i][j])
 
    matriz_n.sort()
    
    matriz_cres = []
    num = 0
    for i in range(0, m):
        line = []
        for j in range(0, n):
            line.append(matriz_n[num])
            num += 1
        matriz_cres.append(line)
    
    print('Matriz em ordem crescente: ')
    for i in range(0, m):
        for j in range(0, n):
            print(matriz_cres[i][j], end=' ')
        print()

m = int(input('linhas : '))
n = int(input('colunas : '))


matriz = []
for l in range(0, m):
    line = []
    for c in range(0, n):
        line.append(int(input('X{}{}: '.format(l + 1, c + 1))))
    matriz.append(line)

matrizt()
