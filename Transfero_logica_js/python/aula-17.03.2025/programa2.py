#Faça um programa para calcular a área de um retângulo

largura = float(input("Digite a largura do retângulo: "))
comprimento = float(input("Digite o comprimento do retângulo: "))

area = largura * comprimento
#Para arredondar o número decimal tem como usar com o f string usando :.numero
print(f"a área do retângulo com as informações inseridas é: {area:.1f}")

#Para arredondar o número decimal sem usar com o f string usando round(variavel,numero decimal)
print(f"a área do retângulo com as informações inseridas é:", round(area,1))