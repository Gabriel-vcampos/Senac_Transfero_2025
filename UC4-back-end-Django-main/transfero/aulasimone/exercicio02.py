#Exercício 2: Leia o conteúdo do arquivo produtos.txt e exiba no console.

with open('produtos.txt' , 'r') as file:
    print(file.read())