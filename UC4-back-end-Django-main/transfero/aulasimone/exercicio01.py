#Exercício
#1: Escreva um arquivo chamado produtos.txt com os seguintes dados:
#Arroz,20
#Feijão,15
#Açúcar,10

with open('produtos.txt' , 'w') as file:
    file.write("Arroz,20 \nFeijão,15 \nAçúcar,10")

with open('produtos.txt' , 'r') as file:
    print(file.read())