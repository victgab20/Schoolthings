#Faça um programa que leia três valores inteiros, dia, mes e ano, respectivamente.
# O programa deve verificar se a data informada é valida ou invalida


d = int(input(" Digite seu dia de nascimento: "))
m = int(input('Digite seu mês de nascimento: '))
a = int(input(' Digite seu ano de nascimento: '))
v = False

# entradas de números inteiros para a data

if m == 1 or m == 3 or m == 5 or m == 7 or  m == 8 or m == 10 or m == 12:
    if d <= 31:
        v = True
        #verificação dos meses que podem ter 31 dias
elif m == 4 or m == 6 or m == 9 or m == 11:
    if d <= 30:
        v = True
        #verificação dos que chega até os 30
elif m == 2:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 or a == 1500 :
        if d <= 29:
            v = True
            #utilização das dicas do professor
    elif d <= 28:
        v = True
        # ano bissexto

if v:
    print('A data', d,'/', m, '/', a,'é válida')
else:
    print('A data', d,'/', m, '/', a,'é inválida')
