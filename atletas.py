from utils import clear, wait_keypress
from ficheiros import inserir_registo, ler_registos, ler_registos_csv, ler_registos_pandas_csv, ler_registos_pandas_json

class Pessoa:
    def __init__(self, nome, apelido, data_nascimento):
        self.nome = nome
        self.apelido = apelido
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return f"{self.nome} {self.apelido}"
    
    
class Atleta(Pessoa):
    def __init__(self, nome, apelido, data_nascimento, posicao, mao):
        super().__init__(nome, apelido, data_nascimento)
        self.posicao = posicao
        self.mao = mao

    def __str__(self):
        return f"Nome: {self.nome_completo()}\nPosição: {self.posicao}"

lista_atletas = []

def inserir_atleta():
    clear()
    print("### Inserir Novo Atleta ###")
    nome = input("Nome: ")
    apelido = input("Apelido: ")
    data_nascimento = input("Data de Nascimento: ")
    posicao = input("Posição: ")
    mao = input("Mão: ")

    atleta = Atleta(nome, apelido, data_nascimento, posicao, mao)
    lista_atletas.append(atleta)

    inserir_registo(nome, apelido, data_nascimento, posicao, mao)

    print(f"\nSucesso na inserção do atleta: {atleta.nome_completo()}")
    wait_keypress()

def listar_atletas():
    # print("Nome // Data_Nascimento // Posição // Mão")
    # for atleta in lista_atletas:
    #     print(f"{atleta.nome_completo()} // ", end="")
    #     print(f"{atleta.data_nascimento} // ", end="")
    #     print(f"{atleta.posicao} // ", end="")
    #     print(f"{atleta.mao}")

    ler_registos()
    wait_keypress()


def listar_atletas_csv():
    ler_registos_csv()
    wait_keypress()

def listar_atletas_pandas_csv():
    ler_registos_pandas_csv()
    wait_keypress()

def listar_atletas_pandas_json():
    ler_registos_pandas_json()
    wait_keypress()
