#Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário.
#No Brasil, a tabela do Imposto de Renda para pessoas físicas (IRPF) é progressiva, ou seja, as alíquotas aumentam conforme a renda do contribuinte. A tabela é ajustada anualmente e varia de acordo com a faixa de salário. Para o ano de 2024, as faixas de tributação do Imposto de Renda para pessoas físicas são as seguintes:Até R$ 2.112,00: isento (não paga imposto de renda)
#De R$ 2.112,01 até R$ 2.826,65: 7,5% (aplica-se sobre o valor que exceder a R$ 2.112,00)
#De R$ 2.826,66 até R$ 3.751,05: 15% (aplica-se sobre o valor que exceder a R$ 2.826,65)
#De R$ 3.751,06 até R$ 4.664,68: 22,5% (aplica-se sobre o valor que exceder a R$ 3.751,05)
#Acima de R$ 4.664,68: 27,5% (aplica-se sobre o valor que exceder a R$ 4.664,68)

salario = float(input("Digite o salário do funcionário desejado: "))
IRPF = 0
salario_total = 0

if salario >= 2112.01 and salario <= 2826.65:
    IRPF = (salario * 7.5/100)
    salario_total = salario - IRPF
elif salario >= 2826.66 and salario <= 3751.05:
    IRPF = (salario * 15/100)
    salario_total = salario - IRPF
elif salario >= 3751.06 and salario <= 4664.68:
    IRPF = (salario * 22.5/100)
    salario_total = salario - IRPF
elif salario > 4664.68:
    IRPF = (salario * 27.5/100)
    salario_total = salario - IRPF
else:
    print("Salário abaixo de 2112, o salário não será descontado")

print("O salário descontado seria: " , salario_total)

