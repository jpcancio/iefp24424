import csv
import pandas as pd
import matplotlib.pyplot as plt

ficheiro_atletas = "atletas.csv"
ficheiro_atletas_json = "atletas.json"
cabecalho = "Nome,Apelido,Data_Nascimento,Posição,Mão\n"

def inserir_registo(nome, apelido, data_nascimento, posicao, mao):
    try:
        f = open(ficheiro_atletas, "x")
        f.write(cabecalho)
    except FileExistsError:
        f = open(ficheiro_atletas, "a")
        if f.tell() == 0:
            f.write(cabecalho)

    f.write(f"{nome},{apelido},{data_nascimento},{posicao},{mao}\n")
    f.close()

def ler_registos():
    try:
        f = open(ficheiro_atletas, "r")
        cabecalho = f.readline().replace('\n', '').split(",")  # ler a primeira linha para nao exibir a seguir

        for linha in f:
            valores = linha.replace('\n', '').split(",")
            for i in range(len(valores)):
                print(f"{cabecalho[i]}: {valores[i]}")
            print("\n")

        f.close()
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro_atletas} nao foi encontrado.")
    
def ler_registos_csv():
    try:
        f = open(ficheiro_atletas, "r", encoding="utf-8")
        ficheiro = csv.reader(f, delimiter=",")
        for linha in ficheiro:
            print(linha[0], linha[1], linha[2], linha[3], linha[4], sep=" // ") 

        f.close()
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro_atletas} nao foi encontrado.")
    
def ler_registos_pandas_csv():
    try:
        df = pd.read_csv(ficheiro_atletas, encoding="utf-8")
        print(pd.options.display.max_rows)
        print(df)
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro_atletas} nao foi encontrado.")
    
def ler_registos_pandas_json():
    try:
        df = pd.read_json(ficheiro_atletas_json)
        # new_df = df.dropna() # REMOVE LINHAS COM VALORES NULOS
        df["mao"].fillna("Direita", inplace = True) 
        #new_df = df["mao"].fillna("Direita") 

        df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], format='mixed', errors='coerce')


        print(df.head(15))
        print(df.tail(10))
        print(df.info())
        #print(new_df.head(100).to_string())

        
        plt.xlabel("Posicao")
        plt.ylabel("Quantidade")
        plt.title("Atletas por Posição")
        plt.bar(df["posicao"].value_counts().index, df["posicao"].value_counts())

        plt.show()

    except FileNotFoundError:
        print(f"O ficheiro {ficheiro_atletas_json} nao foi encontrado.") 