def start ():
    sair = 0
    while (sair == 0):
        print("[1] - INICIAR JOGO")
        print("[2] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            nome_jogador = input("Informe seu nome: ")
            #carregar_arquivo_personagem()
            welcome()
        elif (opcao == 2):
            sair = 1
        else:
            print("Opção inválida!")

def carregar_arquivo_personagem ():
    arquivo = open('personagens.txt', 'r')
    personagens = arquivo.read().split("\n")
    arquivo.close()

    return personagens

def welcome ():
    print("*"*50)
    print("*                                                *")
    print("\t\tBEM-VINDO AO MUNDO DO REI MALVADO            *")
    print("\t\tDEFENDA SUA HONRA EM BATALHAS MORTAIS        *")
    print("*\tSUAS ESCOLHAS DEFINIRAM O DESTINO DE SUA JORNADA*")
    print("*                                                *")
    print("*"*50)

if (__name__ == "__main__"):
    start()