#5) Escreva um programa que leia o valor de um produto e o percentual de desconto. O programa deve exibir o valor final com o desconto aplicado.

valor_produto = int(input("Digite a seguir o valor do produto: "))

valor_do_percentual = int(input("Digite o percentual de desconto que será inserido: "))

valor_do_desconto = valor_produto * (valor_do_percentual/100)

valor_final = valor_produto - valor_do_desconto
print("O valor com desconto ficou:" , valor_final)