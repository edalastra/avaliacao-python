import os

def start ():
    sair = 0
    while (sair == 0):
        print("\n[1] - INICIAR JOGO")
        print("[2] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            nome_jogador = input("Informe seu nome: ").strip().upper()
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
    #print('\033[32m''\033[0;0m')
    print("*"*58)
    print("")
    print("\t\t\tBEM-VINDO {}, JOVEM GUERREIRO".format(nome_jogador).upper())
    print("\t\t  DEFENDA SUA HONRA EM BATALHAS MORTAIS")
    print("\t  SUAS ESCOLHAS DEFINIRÃO O DESTINO DE SUA JORNADA")
    print("")
    print("*"*58)

    print("Após a queda da Igreja na capital, o caos foi se espalhando aos poucos e agora cabe a você salvar o Reino.\nVocê deve fazer suas escolhas com honra e sabedoria, pois elas afetaram diretamente a sua jornada. Que a força esteja com você...")

    print("\nPara salvar o Reino, você deve chegar a capital para batalhar, entretanto, até lá você terá uma árdua jornada.")
    print("Com cuidado, decida qual caminho você irá tomar: ")
    print("[1] - Ir pelas masmorras")
    print("[2] - Seguir o rio")

    while (True):
        opcao_cenario = int(input("\nDigite sua decisão: "))
        if (opcao_cenario == 1):
            masmorras()
        elif (opcao_cenario == 2):
            seguir_o_rio()
        else:
            print("Decisão inválida!")

def masmorras():
    personagem = carregar_arquivo_personagem()
    print("\nAo se aproximar das masmorras, você avista um velho com armadura feita de pedra, ele é o {}.".format(personagem[0]))
    print("O {} se aproxima de você e vocês começam a conversar. Ele houve a sua história e se impressiona com a sua \nintenção de salvar o reino e decide lhe oferecer ajuda. Você aceita?".format(personagem[0]))
    print("[1] - Aceitar ajuda")
    print("[2] - Negar ajuda")

    while (True):
        opcao_decisao = int(input("\nDigite sua decisão: "))
        if (opcao_decisao == 1):
            aceitou_ajuda()
        elif (opcao_decisao == 2):
            negou_ajuda()
        else:
            print("Decisão inválida!")

def seguir_o_rio():
    print("\nÉ noite quando você chega as margens do Rio das Máguas, seguindo o rio, em direção a capital, você avista uma esbelta mulher admirando a paisagem.")
    print("Tomado por admiração com a beleza da mulher, você decide:")
    print("[1] - Ir conversar com ela")
    print("[2] - Ignora-lá e seguir com sua jornada, afinal, é isso que importa para você")

def aceitou_ajuda():
    print("negou")

def negou_ajuda():
    print("negou")

def conversar_mulher():
    print("conversar")

def ignorar_a_mulher():
    print("ignorou")

if (__name__ == "__main__"):
    start()