class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

def apresentar(self):
    print(f'oi, eu sou {self.nome} e tenho {self.idade} anos.')

pessoa1 = Pessoa("Ana maria" , 20)
apresentar(pessoa1)

class Carro:
    def __init__(self, modelo , placa , ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

def ligar(self, modelo , placa , ano):
    print(f"O Carro de modelo: {self.modelo} , do ano de: {self.ano} com a placa: {self.placa} ligou!")

def parar(self , modelo , placa , ano):
    print(f"O Carro de modelo: {self.modelo} , do ano de: {self.ano} com a placa: {self.placa} parou!")

carro1 = Carro("Honda" , "TR5431GF" , 2003)
ligar(carro1)