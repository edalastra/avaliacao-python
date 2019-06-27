jogador = {
    'amigos': [],
    'inimigos': [],
    'caminhos': [],
    'vida': 100,
    'sabedoria': 100,
    'arma': 'soco'
}
ataques = {
    'fraco' : 20,
    'medio' : 50,
    'forte' : 70,
    'especial' : 100
}

def carregar_arquivo_personagem ():
    arquivo = open('personagens.txt', 'r')
    personagens = arquivo.read().split("\n")
    arquivo.close()

    return personagens

personagens = carregar_arquivo_personagem()

def start ():
    sair = 0
    while (sair == 0):
        print("\n[1] - INICIAR JOGO")
        print("[2] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            nome_jogador = input("Informe seu nome: ").strip().upper()
            welcome(nome_jogador)
        elif (opcao == 2):
            sair = 1
        else:
            print("Opção inválida!")

def welcome (nome_jogador):
    print("*"*58)
    print("")
    print("\t\t\tBEM-VINDO {}, JOVEM GUERREIRO(A)".format(nome_jogador).upper())
    print("\t\t  DEFENDA SUA HONRA EM BATALHAS MORTAIS")
    print("\t  SUAS ESCOLHAS DEFINIRÃO O DESTINO DE SUA JORNADA")
    print("")
    print("*"*58)

    print("Após a queda da Igreja na capital, o caos foi se espalhando, e o mundo foi dominado pelo {}, e, agora cabe a você salvar o Reino.\nVocê deve fazer suas escolhas com honra e sabedoria, pois elas afetarão diretamente a sua jornada. Que a força esteja com você...".format(personagens[0]))

    jogador['caminhos'].append(escolha_caminho())

def escolha_caminho():
    print("\nPara salvar o Reino, você deve chegar a capital para batalhar, entretanto, até lá você terá uma árdua jornada.")
    print("Com cuidado, decida qual caminho você irá tomar: ")
    print("[1] - Ir pelas masmorras")
    print("[2] - Seguir o rio")

    while (True):
        opcao_cenario = int(input("\nDigite sua decisão: "))
        if (opcao_cenario == 1):
            jogador['amigos'].append(masmorras())
            return "masmorras"
        elif (opcao_cenario == 2):
            seguir_o_rio()
            return "rio"
        else:
            print("Decisão inválida!")

def masmorras():
    print("\nAo se aproximar das masmorras, você avista um velho com armadura feita de pedra, ele é o {}.".format(personagens[1]))
    print("O {} se aproxima de você e vocês começam a conversar. Ele houve a sua história e se impressiona com a sua \nintenção de salvar o reino e decide lhe oferecer ajuda. Você aceita?".format(personagens[1]))
    print("[1] - Aceitar ajuda")
    print("[2] - Negar ajuda")

    while (True):
        opcao_decisao = int(input("\nDigite sua decisão: "))
        if (opcao_decisao == 1):
            aceitou_ajuda()
            return personagens[1]
        elif (opcao_decisao == 2):
            negou_ajuda()
        else:
            print("Decisão inválida!")

def seguir_o_rio():
    print("\nÉ noite quando você chega as margens do Rio das Máguas, seguindo o rio, em direção a capital, você avista uma esbelta mulher admirando a paisagem.")
    print("Tomado por admiração com a beleza da mulher, você decide:")
    print("[1] - Ir conversar com ela")
    print("[2] - Ignora-lá e seguir com sua jornada, afinal, é isso que importa para você")

    while (True):
        opcao_decisao = int(input("\nDigite sua decisão: "))
        if (opcao_decisao == 1):
            conversar_mulher()
        elif (opcao_decisao == 2):
            ignorar_a_mulher()
        else:
            print("Decisão inválida!")

def aceitou_ajuda():
    print("Ótima decisão! Agora, o {} é seu amigo e lhe forneceu uma de suas melhores armaduras.".format(personagens[1]))
    print("Você obteve 20 pontos de vida, entretanto, o {} irá lhe acompanhar em sua jornada até a capital e irá atrasar sua viajem.".format(personagens[1]))
    jogador['vida'] += 20

def negou_ajuda():
    print("Você negou ajuda, sua jornada continuará, entretanto, o {} não lhe ajudará, e, você deixou de ganhar recompensas.".format(personagens[1]))

def conversar_mulher():
    print("A mulher revelou ser a {}, fiel ajudante do {}, responsável pela falência da igreja e causador de todo o mal que o Reino sofre.".format(personagens[2], personagens[0]))
    print("A {} lhe menosprezou dizendo que você é fraco e por isso não irá lhe enfrentar agora. Ela mandou você se fortalecer e jurou matar-lhe futuramente.".format(personagens[2]))

def ignorar_a_mulher():
    print("Ignorar a mulher foi uma sábia decisão, pois ela era a {}, fiel ajudante do {}. O qual você precisa enfrentar para acabar com a escuridão que assombra o reino.".format(personagens[2], personagens[0]))
    print("A {} tentará impedir-lhe de matar o {} a todo custo. Siga sua jornada com cuidado...".format(personagens[2], personagens[0]))
    print("Você ganhou 20 pontos de sabedoria.")
    jogador['sabedoria'] += 20

if (__name__ == "__main__"):
    start()