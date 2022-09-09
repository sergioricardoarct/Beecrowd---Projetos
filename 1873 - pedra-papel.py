qtd_jogadas = int(input())

for i in range(qtd_jogadas):
    jogo = input().split()
    jogo_1 = jogo[0]
    jogo_2 = jogo[1]
    if (jogo_1 == jogo_2):
        print('empate')
    elif(jogo_1 == 'tesoura' and (jogo_2 == 'papel' or jogo_2 == 'lagarto')):
        print('rajesh')
    elif(jogo_1 == 'papel' and (jogo_2 == 'pedra' or jogo_2 == 'spock')):
        print('rajesh')
    elif(jogo_1 == 'pedra' and (jogo_2 == 'lagarto' or jogo_2 == 'tesoura')):
        print('rajesh')
    elif(jogo_1 == 'lagarto' and (jogo_2 == 'spock' or jogo_2 == 'papel')):
        print('rajesh')
    elif(jogo_1 == 'spock' and (jogo_2 == 'tesoura' or jogo_2 == 'pedra')):
        print('rajesh')
    else:
        print('sheldon')