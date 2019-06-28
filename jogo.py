from random import randrange

def carregar_arquivo (nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    itens = arquivo.read().split("\n")
    arquivo.close()

    return itens

personagens = carregar_arquivo('personagens.txt')

ataques_inimigo_primeira_batalha = carregar_arquivo('ataques-inimigos/primeira-batalha.txt')
ataques_inimigo_segunda_batalha = carregar_arquivo('ataques-inimigos/segunda-batalha.txt')
ataques_inimigo_terceira_batalha = carregar_arquivo('ataques-inimigos/terceira-batalha.txt')

jogador = {
    'score' : 0,
    'nome' : '',
    'amigos': [],
    'inimigos': [],
    'caminhos': [],
    'vida': 100,
    "ataques" : ["magia", "fogo", "fisico", "espada"],
    'sabedoria' : 100
}

personagem1 = {
    'nome' : personagens[0],
    'vida' : 120,
}
personagem2 = {
    'nome' : personagens[1],
    'vida' : 100,
}
personagem3 = {
    'nome' : personagens[2],
    'vida' : 100,
}
personagem4 = {
    'nome' : personagens[3],
    'vida' : 100,
}

def start ():
    sair = 0
    while (sair == 0):
        print("\n[1] - INICIAR JOGO")
        print("[2] - ACESSAR O HISTORICO DE JOGADORES")
        print("[3] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            jogador['nome'] = input("Informe seu nome: ").strip().upper()
            welcome()
        elif(opcao):
            ranking()
        elif (opcao == 3):
            sair = 1
        else:
            print("Opção inválida!")

def welcome ():
    print("*"*58)
    print("")
    print("\t\t\tBEM-VINDO {}, JOVEM GUERREIRO(A)".format(jogador['nome']))
    print("\t\t  DEFENDA SUA HONRA EM BATALHAS MORTAIS")
    print("\t  SUAS ESCOLHAS DEFINIRÃO O DESTINO DE SUA JORNADA")
    print("")
    print("*"*58)

    print("Após a queda da Igreja na capital, o caos foi se espalhando, e o mundo foi dominado pelo {}, e, agora cabe a você salvar o Reino.\nVocê deve fazer suas escolhas com honra e sabedoria, pois elas afetarão diretamente a sua jornada. Que a força esteja com você...".format(personagem1['nome']))

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
    print("\nAo se aproximar das masmorras, você avista um velho com armadura feita de pedra, ele é o {}.".format(personagem2['nome']))
    print("O {} se aproxima de você e vocês começam a conversar. Ele houve a sua história e se impressiona com a sua \nintenção de salvar o reino e decide lhe oferecer ajuda. Você aceita?".format(personagem2['nome']))
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
    print("Ótima decisão! Agora, o {} é seu amigo e lhe forneceu uma de suas melhores armaduras.".format(personagem2['nome']))
    print("Você obteve 20 pontos de vida, entretanto, o {} irá lhe acompanhar em sua jornada até a capital e irá atrasar sua viajem.".format(personagem1['nome']))
    jogador['vida'] += 20
    print("")
    chegando_a_capital()

def negou_ajuda():
    print("Você negou ajuda, sua jornada continuará, entretanto, o {} não lhe ajudará, e, você deixou de ganhar recompensas.".format(personagem2['nome']))
    print("")
    chegando_a_capital()

def conversar_mulher():
    print("A mulher revelou ser a {}, fiel ajudante do {}, responsável pela falência da igreja e causador de todo o mal que o Reino sofre.".format(personagem3['nome'], personagem1['nome']))
    print("A {} lhe menosprezou dizendo que você é fraco e por isso não irá lhe enfrentar agora. Ela mandou você se fortalecer e jurou matar-lhe futuramente.".format(personagem3['nome']))
    print("")
    chegando_a_capital()

def ignorar_a_mulher():
    print("Ignorar a mulher foi uma sábia decisão, pois ela era a {}, fiel ajudante do {}. O qual você precisa enfrentar para acabar com a escuridão que assombra o reino.".format(personagem3['nome'], personagem1['nome']))
    print("A {} tentará impedir-lhe de matar o {} a todo custo. Siga sua jornada com cuidado...".format(personagem3['nome'], personagem1['nome']))
    print("Você ganhou 20 pontos de sabedoria.")
    jogador['sabedoria'] += 20
    print("")
    chegando_a_capital()

def chegando_a_capital():
    print("Finalmente você se aproxima da capital e a avista em chamas, ouve gritos distantes e se apressa para chegar o quanto antes para derrotar seus inimigos.")
    print("Ao se aproximar de uma casa em destroços, o {}, braço direito do {} lhe desafia para uma batalha.".format(personagem4['nome'], personagem1['nome']))
    print("Caso você seja derrotado, o reino irá ruir. Porém, caso ganhe, você irá ganhar recompensas. Você decide:")
    print("[1] - Fugir")
    print("[2] - Batalhar")

    while (True):
        opcao_decisao = int(input("\nDigite sua decisão: "))
        if (opcao_decisao == 1):
            seguir_jornada()
        elif (opcao_decisao == 2):
            primeira_batalha()
        else:
            print("Decisão inválida!")

def seguir_jornada():
    print("Fugindo do {}, envergonhado pela desonra, você acaba indo descansar embaixo da Ponte das Lamentações e acaba encontrando um velho comerciante que houve sua história e lhe presenteia com a espada Elixir, a matadora de Dragões.".format(personagem4['nome']))
    print("Seguindo a jornada com o objetivo de salvar o Reino, ao longe você avista a {}, a qual jurou matar todos que desafiam o Mago Negro!".format(personagem3['nome']))
    segunda_batalha()

def primeira_batalha():
    print("*"*40)
    print("\t\tPRIMEIRA BATALHA")
    print("\t{} VS {}".format(jogador['nome'], personagem4['nome'].upper()))
    print("*"*40)

    while (personagem4['vida'] > 0 and jogador['vida'] > 0):
        print("\nSelecione seu ataque:")
        print("[1] - Ataque de {}".format(jogador['ataques'][0]))
        print("[2] - Ataque de {}".format(jogador['ataques'][1]))
        print("[3] - Ataque de {}".format(jogador['ataques'][2]))

        ataque_aleatorio = randrange(0, len(ataques_inimigo_primeira_batalha))
        personagem4['vida'] -= randrange(20, 50)
        jogador['vida'] -= randrange(20,40)
        opcao_decisao = int(input("\nDigite sua decisão: "))
        if (opcao_decisao == 1):
            print("O {} apresenta resistência contra magia. Você o atingiu com 50 de dano.".format(personagem4['nome']))

            print('{} {}'.format(personagem4['nome'], ataques_inimigo_primeira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem4['nome'], personagem4['vida']))

        elif (opcao_decisao == 2):
            print("Você atingiu o ponto fraco do {}!".format(personagem4['nome']))

            print('{} {}'.format(personagem4['nome'], ataques_inimigo_primeira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem4['nome'], personagem4['vida']))

        elif (opcao_decisao == 3):
            print("Você o acertou em cheio! Entretanto, a armadura do {} é muito forte!".format(personagem4['nome']))

            print('{} {}'.format(personagem4['nome'], ataques_inimigo_primeira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem4['nome'], personagem4['vida']))

        else:
            print("Decisão inválida!")

    if (personagem4['vida'] <= 0 and jogador['vida'] > 0):
        print("\nParabéns! Você venceu sua primeira batalha! E como recompensa você pegou a espada Elixir, pertencente ao {}!".format(personagem4['nome']))
        jogador['score'] += jogador['vida']
        print('Sua pontuação atual é : {}'.format(jogador['score']))
        jogador['vida'] = 100
        segunda_batalha()

    elif (personagem4['vida'] <= 0 and jogador['vida'] <= 0):
        print("Você atingiu o {} em cheio, porém, ele revidou e você também morreu!".format(personagem4['nome']))
        game_over()

    else:
        print("YOU DIED!")
        game_over()

def segunda_batalha():
    print("Sem descanso, você deve enfrenta-lá a todo custo para poder derrotar o {}!".format(personagem1['nome']))
    print("")
    print("*" * 40)
    print("\t\tSEGUNDA BATALHA")
    print("\t{} VS {}".format(jogador['nome'], personagem3['nome'].upper()))
    print("*" * 40)

    while (personagem3['vida'] > 0 and jogador['vida'] > 0):

        print("\nSelecione seu ataque:")
        print("[1] - Ataque de {}".format(jogador['ataques'][0]))
        print("[2] - Ataque de {}".format(jogador['ataques'][1]))
        print("[3] - Ataque de {}".format(jogador['ataques'][2]))
        print("[4] - Ataque de {}".format(jogador['ataques'][3]))

        personagem3['vida'] -= randrange(20, 50)
        jogador['vida'] -= randrange(20, 40)
        ataque_aleatorio = randrange(0, len(ataques_inimigo_segunda_batalha))
        opcao_decisao = int(input("\nDigite sua decisão: "))

        if (opcao_decisao == 1):
            print("Booom! A magia a deixou confusa e vulnerável, e o ataque certo a matará.".format(personagem3['nome']))


            print('{} {}'.format(personagem3['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(personagem3['nome'] ,personagem3['vida']))

        elif (opcao_decisao == 2):
            print("Este ataque não a fez nem cóssegas!")

            print('{} {}'.format(personagem3['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(personagem3['nome'], personagem3['vida']))

        elif (opcao_decisao == 3):
            print("Em cheio! Ela está com dificuldades de se manter em pé!")

            print('{} {}'.format(personagem3['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(personagem3['nome'], personagem3['vida']))

        elif (opcao_decisao == 4):
            print("Você a perfurou com sua Elixir!")

            print('{} {}'.format(personagem3['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(personagem3['nome'], personagem3['vida']))

        else:
            print("Decisão inválida!")

    if (personagem3['vida'] <= 0 and jogador['vida'] > 0):
        print("\nParabéns! Você venceu sua segunda batalha...\n")
        jogador['score'] += jogador['vida']
        print('Sua pontuação atual é : {}'.format(jogador['score']))
        jogador['vida'] = 100
        desfecho()


    elif (personagem3['vida'] <= 0 and jogador['vida'] <= 0):
        print("Você atingiu a {} em cheio, porém, ela revidou e você também morreu!".format(personagem3['nome']))
        game_over()

    else:
        print("YOU DIED!")
        game_over()

def desfecho ():
    print("Agora, após confrontos e batalhas, você está próximo de finalizar sua jornada e salvar o Reino! Mas toda salvação requer um esforço e sua última batalha será contra o {}!".format(personagem1['nome']))
    print("O {} sempre está na catedral espalhando suas pregações de ódio, você tem a oportunidade de pegá-lo desprevinido e o matar, o que você decide?".format(personagem1['nome']))

    print("[1] - Atacá-lo em stealth")
    print("[2] - Confrontá-lo face a face")

    opcao_decisao = int(input("Digite sua decisão: "))

    if (opcao_decisao == 1):
        print("Você vai por trás da catedral, camuflado entre os destroços e a mata cinza, pula a janela e avista o Mago Negro sozinho no altar, que aparentemene, está cochilando.")
        print("Você, em silêncio, vai na direção dele, saca sua Elixir e...")
        print("[1] - Perfura seu pulmão")
        print("[2] - Repensa e o confronta face a face")
        decisao_final1 = int(input("Digite sua decisão: "))
        decisao_final(decisao_final1)

    elif (opcao_decisao == 2):
        face_a_face()
    else:
        print("Opção inválida!")

def decisao_final(decisao):
    while (True):
        if (decisao == 1):
            print("Ao se aproximar do {} com a intenção de matá-lo desprevinido, ele disperta do sono ao sentir sua presença e percebe suas intenções e a batalha inicia!".format(personagem1['nome']))
            terceira_batalha()
        elif(decisao == 2):
            face_a_face()
        else:
            print("Opção inválida")

def face_a_face():
    print("Você o vê cochilando no altar, e grita: As trevas irão voltar para onde vieram! O {}, com cara de desprezo imediatamente invoca sua magia e parte pra batalha!".format(personagem1['nome']))
    terceira_batalha()

def terceira_batalha ():
    print("")
    print("*" * 40)
    print("\t\tTERCEIRA BATALHA")
    print("\t{} VS {}".format(jogador['nome'], personagem1['nome'].upper()))
    print("*" * 40)

    while (personagem1['vida'] > 0 and jogador['vida'] > 0):

        print("\nSelecione seu ataque:")
        print("[1] - Ataque de {}".format(jogador['ataques'][0]))
        print("[2] - Ataque de {}".format(jogador['ataques'][1]))
        print("[3] - Ataque de {}".format(jogador['ataques'][2]))
        print("[4] - Ataque de {}".format(jogador['ataques'][3]))
        personagem1['vida'] -= randrange(20, 50)
        jogador['vida'] -= randrange(20, 40)
        ataque_aleatorio = randrange(0, len(ataques_inimigo_terceira_batalha))
        opcao_decisao = int(input("\nDigite sua decisão: "))

        if (opcao_decisao == 1):
            print("A magia não funciona muito bem com o {}, afinal, ele a domina! Tente outra coisa!".format(personagem1['nome']))

            print('{} {}'.format(personagem1['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem1['nome'], personagem1['vida']))
        elif (opcao_decisao == 2):
            print("O fogo o queima como um carvão! Muito bem!")

            print('{} {}'.format(personagem1['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem1['nome'], personagem1['vida']))
        elif (opcao_decisao == 3):
            print("Com esse golpe ele irá ficar confuso!")

            print('{} {}'.format(personagem1['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem1['nome'], personagem1['vida']))

        elif (opcao_decisao == 4):
            print("Wooow! Você decepou a mão dele, o tornando incapaz de usar o cajado!")

            print('{} {}'.format(personagem1['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(personagem1['nome'], personagem1['vida']))

        else:
            print("Opção inválida")

    if(personagem1['vida'] <= 0 and jogador['vida'] > 0):
        jogador['score'] += jogador['vida']
        print('Sua pontuação atual é : {}'.format(jogador['score']))
        jogador['vida'] = 100
        imprime_mensagem_vencedor()
        game_over()

    elif (personagem1['vida'] <= 0 and jogador['vida'] <= 0):
        print("Você atingiu a {} em cheio, porém, ela revidou e você também morreu!".format(personagem3['nome']))
        game_over()

    else:
        print("YOU DIED!")
        game_over()

def imprime_mensagem_vencedor():
    print("Parabéns, você foi uma vela no escuro e venceu o jogo!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def game_over():
    arquivo = open('score.txt', 'a')
    pontuacao = "{} {}\n".format(jogador["nome"], jogador['score'])
    arquivo.write(pontuacao)
    arquivo.close()

    print("*" * 40)
    print("\t\tF I M  D E  J O G O")
    print("\t\tJOGADOR: {}".format(jogador['nome'].upper()))
    print("\t\tPONTUAÇÃO: {}".format(jogador['score']))
    print("*" * 40)
    print("Deseja jogar novamente?")
    print("[1] - Sim")
    print("[2] - Não")
    restart = int(input("Opção: "))
    if (restart == 1):
        welcome()
    else:
        start()

def ranking():
    rank = carregar_arquivo('score.txt')

    for i in rank:
        print(i)

if (__name__ == "__main__"):
    start()