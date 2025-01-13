import atletas
from utils import clear

def main():
    while True:
        clear()
        print("### APP ANDEBOL CENAS ###")
        print("1. Inserir Atleta")
        print("2. Listar Atletas do Array")
        print("3. Listar Atletas do CSV")
        print("4. Listar Atletas do CSV com Pandas")
        print("5. Listar Atletas do JSON com Pandas")
        print("0. Sair")
        opcao = input("Escolhe a opção:")
        match opcao:
            case "1":
                atletas.inserir_atleta()

            case "2":
                atletas.listar_atletas()

            case "3":
                atletas.listar_atletas_csv()

            case "4":
                atletas.listar_atletas_pandas_csv()

            case "5":
                atletas.listar_atletas_pandas_json()

            case "0":
                print("Obrigado por usar o sistema!")
                break

            case _:  # DEFAULT... VALOR POR DEFEITO... o que sobra
                print ("valor inválido")


if __name__ == "__main__":
    main()