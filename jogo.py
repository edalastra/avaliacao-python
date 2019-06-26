def start ():
    sair = 0
    while (sair == 0):
        print("[1] - INICIAR JOGO")
        print("[2] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            nome_jogador = input("Informe seu nome: ")
            carregar_arquivos()
        elif (opcao == 2):
            sair = 1
        else:
            print("Opção inválida!")

def carregar_arquivos ():
    arquivo = open('personagens.txt', 'r')
    personagens = arquivo.read().split("\n")
    arquivo.close()

    return personagens

if (__name__ == "__main__"):
    start()