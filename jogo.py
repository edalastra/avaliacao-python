def start ():
    sair = 0
    while (sair == 0):
        print("\n[1] - INICIAR JOGO")
        print("[2] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            nome_jogador = input("Informe seu nome: ")
            carregar_arquivo_personagem()
            welcome(nome_jogador)
        elif (opcao == 2):
            sair = 1
        else:
            print("Opção inválida!")

def carregar_arquivo_personagem ():
    arquivo = open('personagens.txt', 'r')
    personagens = arquivo.read().split("\n")
    arquivo.close()

    return personagens

def welcome (nome_jogador):
    print("*"*58)
    print("")
    print("\t\t\tBEM-VINDO {}, JOVEM GUERREIRO".format(nome_jogador).upper())
    print("\t\t  DEFENDA SUA HONRA EM BATALHAS MORTAIS")
    print("\t  SUAS ESCOLHAS DEFINIRAM O DESTINO DE SUA JORNADA")
    print("")
    print("*"*58)

    print("Após a queda da Igreja na capital, o caos foi se espalhando aos poucos e agora cabe a você salvar o Reino.\nVocê deve fazer suas escolhas com honra e sabedoria, pois elas afetaram diretamente a sua jornada. Que a força esteja com você.")

    

if (__name__ == "__main__"):
    start()