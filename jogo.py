from random import randrange

def carregar_arquivo (nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    itens = arquivo.read().split("\n")
    arquivo.close()

    return itens

personagens = carregar_arquivo('personagens.txt')

ataques_inimigo_primeira_batalha = carregar_arquivo('ataques-inimigos/primeira-batalha.txt')
ataques_inimigo_segunda_batalha = carregar_arquivo('ataques-inimigos/segunda-batalha.txt')

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
    'vida' : 100,
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
        print("[2] - SAIR\n")
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            jogador['nome'] = input("Informe seu nome: ").strip().upper()
            welcome()
        elif (opcao == 2):
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
        print('\033[32m' + "\nParabéns! Você venceu sua primeira batalha!" +'\033[0;0m' + "E como recompensa você pegou a espada Elixir, pertencente ao {}!".format(personagem4['nome']))
        jogador['vida'] = 100
        segunda_batalha()

    elif (personagem4['vida'] <= 0 and jogador['vida'] <= 0):
        print("Você atingiu o {} em cheio, porém, ele revidou e você também morreu!".format(personagem4['nome']))
        print("Deseja jogar novamente? ([1] - Não)")
        # game over

    else:
        print( '\033[31m' + "YOU DIED! " + '\033[0;0m' + "Deseja jogar novamente? ([1] - Não)")
        # gameover

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
            personagem3['vida'] -= 100

        else:
            print("Decisão inválida!")

    if (personagem3['vida'] <= 0 and jogador['vida'] > 0):
        print("\nParabéns! Você venceu sua segunda batalha...\n")
        jogador['vida'] = 100

    elif (personagem3['vida'] <= 0 and jogador['vida'] <= 0):
        print("Você atingiu a {} em cheio, porém, ela revidou e você também morreu!".format(personagem3['nome']))
        #game over

    else:
        print("YOU DIED! Deseja jogar novamente? ([1] - Não)")
           #gameover

if (__name__ == "__main__"):
    start()
