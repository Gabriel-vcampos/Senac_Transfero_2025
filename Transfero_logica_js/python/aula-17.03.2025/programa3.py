#Ler um número e informar se este número é par ou ímpar

numero = int(input("Informe um número: "))
if numero % 2 ==0:
    print(f"O valor {numero} é par")
else:
    print(f"O valor {numero} é impar")