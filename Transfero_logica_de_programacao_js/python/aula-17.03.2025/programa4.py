#Ler um número e informar se é positivo, negativo ou zero

numero = int(input("Informe um número: "))
if numero > 0 :
    print(f"O valor {numero} é positivo")
elif numero < 0:
    print(f"O valor {numero} é negativo")
else:
    print("O valor é zero!")