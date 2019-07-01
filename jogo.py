# -*- coding: UTF-8 -*-

from random import randrange
import sys

def carregar_arquivo (nome_arquivo):
    arquivo = open(nome_arquivo, 'r', encoding="ISO-8859-1")
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
    'vida': 100,
    "ataques" : ["magia", "fogo", "físico", "espada"],
    'sabedoria' : 100
}

inimigo_principal = {
    'nome' : personagens[0],
    'vida' : 100,
}

ajudante = {
    'nome' : personagens[1],
    'vida' : 100,
}
primeiro_inimigo = {
    'nome' : personagens[3],
    'vida' : 100,
}
segundo_inimigo = {
    'nome' : personagens[2],
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
            jogador['nome'] = input("\nInforme seu nome: ").strip().upper()
            welcome()
        elif(opcao == 2):
            ranking()
        elif (opcao == 3):
            sys.exit()
        else:
            print("Opção inválida!")

def welcome ():
    print("*"*80)
    print("")
    print("\t\t\tBEM-VINDO {}, JOVEM GUERREIRO(A)".format(jogador['nome']))
    print("\t\t  DEFENDA SUA HONRA EM BATALHAS MORTAIS")
    print("\t  SUAS ESCOLHAS DEFINIRÃO O DESTINO DE SUA JORNADA")
    print("")
    print("*"*80)

    print("Após a queda da Igreja na capital, o caos foi se espalhando, e o mundo foi dominado pelo {}, e, agora cabe a você salvar o Reino.\nVocê deve fazer suas escolhas com honra e sabedoria, pois elas afetarão diretamente a sua jornada. Que a força esteja com você...".format(inimigo_principal['nome']))
    escolha_caminho()

def escolha_caminho():
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
    print("\nAo se aproximar das masmorras, você avista um velho com armadura feita de pedra, ele é o {}.".format(ajudante['nome']))
    print("O {} se aproxima de você e vocês começam a conversar. Ele houve a sua história e se impressiona com a sua \nintenção de salvar o reino e decide lhe oferecer ajuda. Você aceita?".format(ajudante['nome']))
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
    print("Ótima decisão! Agora, o {} é seu amigo e lhe forneceu uma de suas melhores armaduras.".format(ajudante['nome']))
    print("Você obteve 25 pontos a mais de vida, entretanto, o {} irá lhe acompanhar em sua jornada até a capital e irá atrasar sua viajem.".format(inimigo_principal['nome']))
    jogador['vida'] += 25
    print("")
    chegando_a_capital()

def negou_ajuda():
    print("Você negou ajuda, sua jornada continuará, entretanto, o {} não lhe ajudará, e, você deixou de ganhar recompensas.".format(ajudante['nome']))
    print("")
    chegando_a_capital()

def conversar_mulher():
    print("A mulher revelou ser a {}, fiel ajudante do {}, responsável pela falência da igreja e causador de todo o mal que o Reino sofre.".format(segundo_inimigo['nome'], inimigo_principal['nome']))
    print("A {} lhe menosprezou dizendo que você é fraco e por isso não irá lhe enfrentar agora. Ela mandou você se fortalecer e jurou matar-lhe futuramente.".format(segundo_inimigo['nome']))
    print("")
    chegando_a_capital()

def ignorar_a_mulher():
    print("Ignorar a mulher foi uma sábia decisão, pois ela era a {}, fiel ajudante do {}. O qual você precisa enfrentar para acabar com a escuridão que assombra o reino.".format(segundo_inimigo['nome'], inimigo_principal['nome']))
    print("A {} tentará impedir-lhe de matar o {} a todo custo. Siga sua jornada com cuidado...".format(segundo_inimigo['nome'], inimigo_principal['nome']))
    print("Você ganhou 20 pontos de sabedoria.")
    jogador['sabedoria'] += 20
    print("")
    chegando_a_capital()

def chegando_a_capital():
    print("Finalmente você se aproxima da capital e a avista em chamas, ouve gritos distantes e se apressa para chegar o quanto antes para derrotar seus inimigos.")
    print("Ao se aproximar de uma casa em destroços, o {}, braço direito do {} lhe desafia para uma batalha.".format(primeiro_inimigo['nome'], inimigo_principal['nome']))
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

def primeira_batalha():
    print("*"*40)
    print("\t\tPRIMEIRA BATALHA")
    print("\t{} VS {}".format(jogador['nome'], primeiro_inimigo['nome'].upper()))
    print("*"*40)

    while (primeiro_inimigo['vida'] > 0 and jogador['vida'] > 0):
        print("\nSelecione seu ataque:")
        print("[1] - Ataque de {}".format(jogador['ataques'][0]))
        print("[2] - Ataque de {}".format(jogador['ataques'][1]))
        print("[3] - Ataque {}".format(jogador['ataques'][2]))

        ataque_aleatorio = randrange(0, len(ataques_inimigo_primeira_batalha))
        primeiro_inimigo['vida'] -= randrange(20, 50)
        jogador['vida'] -= randrange(20,50)
        opcao_decisao = int(input("\nDigite sua decisão: "))
        if (opcao_decisao == 1):
            print("O {} apresenta resistência contra magia. Tente outro!".format(primeiro_inimigo['nome']))

            print('{} {}'.format(primeiro_inimigo['nome'], ataques_inimigo_primeira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(primeiro_inimigo['nome'], primeiro_inimigo['vida']))

        elif (opcao_decisao == 2):
            print("\nVocê atingiu o ponto fraco do {}!".format(primeiro_inimigo['nome']))

            print('{} {}'.format(primeiro_inimigo['nome'], ataques_inimigo_primeira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(primeiro_inimigo['nome'], primeiro_inimigo['vida']))

        elif (opcao_decisao == 3):
            print("Você o acertou em cheio! Entretanto, a armadura do {} é muito forte!".format(primeiro_inimigo['nome']))

            print('{} {}'.format(primeiro_inimigo['nome'], ataques_inimigo_primeira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(primeiro_inimigo['nome'], primeiro_inimigo['vida']))

        else:
            print("Decisão inválida!")

    if (primeiro_inimigo['vida'] <= 0 and jogador['vida'] > 0):
        print("\nParabéns! Você venceu sua primeira batalha! E como recompensa você pegou a espada Elixir, pertencente ao {}!".format(primeiro_inimigo['nome']))
        jogador['score'] += jogador['vida']
        print('Sua pontuação atual é: {} pontos'.format(jogador['score']))
        jogador['vida'] = 100
        segunda_batalha()

    elif (primeiro_inimigo['vida'] <= 0 and jogador['vida'] <= 0):
        print("\nVocê atingiu o {} em cheio, porém, ele revidou e você também morreu!\n".format(primeiro_inimigo['nome']))
        game_over()

    else:
        print("YOU DIED!")
        game_over()

def seguir_jornada():
    print("Fugindo do {}, envergonhado pela desonra, você acaba indo descansar embaixo da Ponte das Lamentações e acaba encontrando um velho comerciante que houve sua história e lhe presenteia com a espada Elixir, a matadora de Dragões.".format(primeiro_inimigo['nome']))
    segunda_batalha()

def segunda_batalha():
    print("\nSeguindo a jornada com o objetivo de salvar o Reino, ao longe você avista a {}, a qual jurou matar todos que desafiam o {}!".format(segundo_inimigo['nome'], inimigo_principal['nome']))
    print("Sem descanso, você deve enfrenta-lá a todo custo para poder derrotar o {}!".format(inimigo_principal['nome']))
    print("")
    print("*" * 40)
    print("\t\tSEGUNDA BATALHA")
    print("\t{} VS {}".format(jogador['nome'], segundo_inimigo['nome'].upper()))
    print("*" * 40)

    while (segundo_inimigo['vida'] > 0 and jogador['vida'] > 0):

        print("\nSelecione seu ataque:")
        print("[1] - Ataque de {}".format(jogador['ataques'][0]))
        print("[2] - Ataque de {}".format(jogador['ataques'][1]))
        print("[3] - Ataque {}".format(jogador['ataques'][2]))
        print("[4] - Ataque de {}".format(jogador['ataques'][3]))

        segundo_inimigo['vida'] -= randrange(20, 50)
        jogador['vida'] -= randrange(20, 50)
        ataque_aleatorio = randrange(0, len(ataques_inimigo_segunda_batalha))
        opcao_decisao = int(input("\nDigite sua decisão: "))

        if (opcao_decisao == 1):
            print("Booom! A magia a deixou confusa e vulnerável, e o ataque certo a matará.".format(segundo_inimigo['nome']))

            print('{} {}'.format(segundo_inimigo['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(segundo_inimigo['nome'] ,segundo_inimigo['vida']))

        elif (opcao_decisao == 2):
            print("Este ataque não a fez nem cóssegas!")

            print('{} {}'.format(segundo_inimigo['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(segundo_inimigo['nome'], segundo_inimigo['vida']))

        elif (opcao_decisao == 3):
            print("Em cheio! Ela está com dificuldades de se manter em pé!")

            print('{} {}'.format(segundo_inimigo['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(segundo_inimigo['nome'], segundo_inimigo['vida']))

        elif (opcao_decisao == 4):
            print("Você a perfurou com sua Elixir!")

            print('{} {}'.format(segundo_inimigo['nome'], ataques_inimigo_segunda_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP da {}: {}'.format(segundo_inimigo['nome'], segundo_inimigo['vida']))

        else:
            print("Decisão inválida!")

    if (segundo_inimigo['vida'] <= 0 and jogador['vida'] > 0):
        print("\nParabéns! Você venceu sua segunda batalha...\n")
        jogador['score'] += jogador['vida']
        print('Sua pontuação atual é: {} pontos'.format(jogador['score']))
        jogador['vida'] = 100
        desfecho()


    elif (segundo_inimigo['vida'] <= 0 and jogador['vida'] <= 0):
        print("\nVocê atingiu a {} em cheio, porém, ela revidou e você também morreu!\n".format(segundo_inimigo['nome']))
        game_over()

    else:
        print("YOU DIED!")
        game_over()

def desfecho ():
    print("\nAgora, após confrontos e batalhas, você está próximo de finalizar sua jornada e salvar o Reino! Mas toda salvação requer um esforço e sua última batalha será contra o {}!".format(inimigo_principal['nome']))
    print("\nO {} sempre está na catedral espalhando suas pregações de ódio, você tem a oportunidade de pegá-lo desprevinido e o matar, o que você decide?".format(inimigo_principal['nome']))

    print("[1] - Atacá-lo em stealth")
    print("[2] - Confrontá-lo face a face")

    opcao_decisao = int(input("\nDigite sua decisão: "))

    if (opcao_decisao == 1):
        print("\nVocê vai por trás da catedral, camuflado entre os destroços e a mata cinza, pula a janela e avista o {} sozinho no altar, que aparentemene, está cochilando.".format(inimigo_principal['nome']))
        print("Você, em silêncio, vai na direção dele, saca sua Elixir e...")
        print("[1] - Perfura seu pulmão")
        print("[2] - Repensa e o confronta face a face")
        decisao_final1 = int(input("\nDigite sua decisão: "))
        decisao_final(decisao_final1)

    elif (opcao_decisao == 2):
        face_a_face()
    else:
        print("Opção inválida!")

def decisao_final(decisao):
    while (True):
        if (decisao == 1):
            print("Ao se aproximar do {} com a intenção de matá-lo desprevinido, ele disperta do sono ao sentir sua presença e percebe suas intenções e a batalha inicia!".format(inimigo_principal['nome']))
            terceira_batalha()
        elif(decisao == 2):
            face_a_face()
        else:
            print("Opção inválida")

def face_a_face():
    print("\nVocê o vê cochilando no altar, e grita: As trevas irão voltar para onde vieram! O {}, com cara de desprezo imediatamente invoca sua magia e parte pra batalha!".format(inimigo_principal['nome']))
    terceira_batalha()

def terceira_batalha ():
    print("")
    print("*" * 40)
    print("\t\tTERCEIRA BATALHA")
    print("\t{} VS {}".format(jogador['nome'], inimigo_principal['nome'].upper()))
    print("*" * 40)

    while (inimigo_principal['vida'] > 0 and jogador['vida'] > 0):

        print("\nSelecione seu ataque:")
        print("[1] - Ataque de {}".format(jogador['ataques'][0]))
        print("[2] - Ataque de {}".format(jogador['ataques'][1]))
        print("[3] - Ataque {}".format(jogador['ataques'][2]))
        print("[4] - Ataque de {}".format(jogador['ataques'][3]))
        inimigo_principal['vida'] -= randrange(20, 50)
        jogador['vida'] -= randrange(20, 50)
        ataque_aleatorio = randrange(0, len(ataques_inimigo_terceira_batalha))
        opcao_decisao = int(input("\nDigite sua decisão: "))

        if (opcao_decisao == 1):
            print("A magia não funciona muito bem com o {}, afinal, ele a domina! Tente outra coisa!".format(inimigo_principal['nome']))

            print('{} {}'.format(inimigo_principal['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(inimigo_principal['nome'], inimigo_principal['vida']))
        elif (opcao_decisao == 2):
            print("O fogo o queima como um carvão! Muito bem!")

            print('{} {}'.format(inimigo_principal['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(inimigo_principal['nome'], inimigo_principal['vida']))
        elif (opcao_decisao == 3):
            print("Com esse golpe ele irá ficar confuso!")

            print('{} {}'.format(inimigo_principal['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(inimigo_principal['nome'], inimigo_principal['vida']))

        elif (opcao_decisao == 4):
            print("Wooow! Você decepou a mão dele, o tornando incapaz de usar o cajado!")

            print('{} {}'.format(inimigo_principal['nome'], ataques_inimigo_terceira_batalha[ataque_aleatorio]))

            print("\nSeu HP: {}".format(jogador['vida']))
            print('HP do {}: {}'.format(inimigo_principal['nome'], inimigo_principal['vida']))

        else:
            print("Opção inválida")

    if(inimigo_principal['vida'] <= 0 and jogador['vida'] > 0):
        print("Você derrotou o {} e salvou o Reino!".format(inimigo_principal['nome']))
        jogador['score'] += jogador['vida']
        jogador['vida'] = 100
        imprime_mensagem_vencedor()
        game_over()

    elif (inimigo_principal['vida'] <= 0 and jogador['vida'] <= 0):
        print("\nVocê atingiu o {} em cheio, porém, ele revidou e você também morreu!\n".format(inimigo_principal['nome']))
        game_over()

    else:
        print("YOU DIED!")
        game_over()

def imprime_mensagem_vencedor():
    print("Parabéns, você foi uma vela no escuro!")
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
    print("\n\t\tF I M  D E  J O G O")
    print("\n\t\tJOGADOR: {}".format(jogador['nome'].upper()))
    print("\t\tPONTUAÇÃO: {}\n".format(jogador['score']))
    print("*" * 40)
    print("\nDeseja jogar novamente?")
    print("[1] - Sim")
    print("[2] - Não")
    restart = int(input("\nOpção: "))
    if (restart == 1):
        inimigo_principal['vida'] = 100
        ajudante['vida'] = 100
        ajudante['vida'] = 100
        jogador['vida'] = 100
        welcome()
    elif (restart == 2):
        sys.exit()
    else:
        print("Opção inválida!")

def ranking():
    rank = carregar_arquivo('score.txt')

    for i in rank:
        print(i)

if (__name__ == "__main__"):
    start()