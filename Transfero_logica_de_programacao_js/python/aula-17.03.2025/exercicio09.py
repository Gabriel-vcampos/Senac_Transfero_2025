#9) Crie um programa que calcule o valor total de uma compra feita em várias parcelas. Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.

valor_da_compra = float(input("Digite a seguir o valor total da sua compra: "))
valor_parcelas = int(input("Digite a seguir a quantidade de parcelas que deseja inserir no produto: "))

valor_parcelado = valor_da_compra / valor_parcelas

if valor_da_compra > 1000:
    valor_com_juros = valor_da_compra * 5/100
    valor_total = valor_da_compra + valor_com_juros
    valor_total_parcelado = valor_total / valor_parcelas
    print("O valor ficou acima de R$ 1000,00 , logo foi aplicado juros de 5% , O valor ficou sem juros parcelado em: " , valor_parcelas , "x" , " de: " , valor_total_parcelado)
else:
    print("O valor ficou sem juros parcelado em: " , valor_parcelas , "x" , " de: " , valor_parcelado)