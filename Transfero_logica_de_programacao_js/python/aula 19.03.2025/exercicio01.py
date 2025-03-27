#1. Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. Exiba a soma de todos os números positivos digitados.
soma = 0
while True:
    numero = int(input("Olá, Digite um número:"))
    if numero > 0:
        soma += numero
    else:
        break
print(soma)
