#caputurar erro por divisão e erro por dado inválido
try:
    x = int(input("Digite um número: "))
    resultado = 10/x
    print(round(resultado,2))
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")
except ValueError:
    print("Erro: só é permitida a entrada de números")