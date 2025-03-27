# usando o finally para limpeza
try:
    arquivo = open('dados.txt')
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    if 'arquivo' in locals():
        arquivo.close()
        print('arquivo fechado com sucesso')