#2. Escreva um programa que exiba a tabuada de multiplicação de um número digitado pelo usuário, de 1 a 10.
numero = int(input("Digite um número para ser exibido a tabuada:"))
x = 0
for x in range(0 , 11):
        resultado = numero * x
        print("O número: " , numero , " x " , x , " é igual a:" , resultado)
        x += 1
        continue

