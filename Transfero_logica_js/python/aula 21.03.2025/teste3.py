# Definir a própria exceção. Criar manualmente

try:
    idade = int(input("Digite sua idade"))
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    print(idade)
except ValueError as ve:

    print(f"Erro: {ve}")