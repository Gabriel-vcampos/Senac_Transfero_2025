with open('nomes.txt' , 'w') as file:
    file.write('Ella\nBlitz\nAsh')
    file.write('\n25 anos \n38 anos \n32 anos')


with open('nomes.txt' , 'r') as file:
    print(file.read())
