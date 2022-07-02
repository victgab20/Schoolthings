#Faça um programa em Python que leia uma string podendo conter letras do alfabeto (maiúsculas
#e minúsculas), números e espaços em branco. Após leitura, imprimir uma string resultante contendo
#apenas as letras do alfabeto, com as vogais em maiúsculo, sem os números e sem os espaços em branco

#parte do código que apaga os números

nome = input("digite sua string: ")
nome2 = ''.join([i for i in nome if not i.isdigit()])

#a parte do código que subistitui os espaços por nada

nome3 = nome2.replace(" ", '')
#parte que coloca as vogais em maiusculo
vogais = 'aeiouAEIOU'
lista=[]
for letra in nome3:
    if letra in vogais:
        lista.append(letra.upper())
    else:
        lista.append(letra)
junto = ''.join(lista)
print(junto)
