#7) Escreva um programa que receba três números inteiros e determine qual deles é o maior.

numero_1 = int(input("Digite um número a seguir:"))
numero_2 = int(input("Digite outro número a seguir:"))
numero_3 = int(input("Digite outro número a seguir:"))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("O número: " , numero_1 , " é o maior!")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("O número: " , numero_2 , "é o maior! ")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print("O número: " , numero_3 , "é o maior! ")
else:
    print("Os números são iguais, portanto não tem maior")