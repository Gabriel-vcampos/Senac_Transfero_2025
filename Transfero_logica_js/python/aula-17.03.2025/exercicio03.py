#3) Crie um programa que leia um valor em reais (R$) e mostre o valor convertido em dólares (US$), considerando uma taxa de câmbio fornecida pelo usuário.

valor_reais = float(input("Digite a seguir o valor em reais: "))
valor_dolar = valor_reais / 5.70
print(f"O valor em dólar é: {valor_dolar:.1f}")
