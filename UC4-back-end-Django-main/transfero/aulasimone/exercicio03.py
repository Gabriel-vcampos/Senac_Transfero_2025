#Exercício 3: Adicione um produto ao arquivo usando o código
#Python.

with open('produtos.txt' , 'a') as file:
    file.write("leite: 40")

    with open('produtos.txt' , 'r') as file:
        print(file.read())