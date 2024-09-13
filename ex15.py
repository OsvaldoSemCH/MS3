## https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/trabalho_jogovelha.c

tab = [['-','-','-'],['-','-','-'],['-','-','-']]

def zerarmatriz():
    for i in range(3):
        for j in range(3):
            tab[i][j] = '-'
            
def vencedor():
    if(
        (tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2] and  tab[0][2] != '-') or 
        (tab[1][0] == tab[1][1] and tab[1][1] == tab[1][2] and  tab[1][2] != '-') or  
        (tab[2][0] == tab[2][1] and tab[2][1] == tab[2][2] and  tab[2][2] != '-') or
        (tab[0][0] == tab[1][0] and tab[1][0] == tab[2][0] and  tab[2][0] != '-') or
        (tab[0][1] == tab[1][1] and tab[1][1] == tab[2][1] and  tab[2][1] != '-') or
        (tab[0][2] == tab[1][2] and tab[1][2] == tab[2][2] and  tab[2][2] != '-') or
        (tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and  tab[2][2] != '-') or
        (tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and  tab[2][0] != '-')
    ):
        return 1
    else:
        return 0
    
def validador(p_linha : int, p_coluna : int):
    if(tab[p_linha][p_coluna] == 'X' or tab[p_linha][p_coluna] == 'O' ):
        print("Lugar ocupado.")
        return 0
    elif(p_linha > 2 or p_coluna > 2 or p_linha < 0 or p_coluna < 0):
        print("Valor incorreto.")
        return 0
    else:
        return 1
    
def mostra_velha():
    print(f"\n")
    print(f" 0     1     2 \n")
    print(f"      |   |   ")
    print(f"0   {tab[0][0]} | {tab[0][1]} | {tab[0][2]} ")
    print(f"   ___|___|___")
    print(f"      |   |   ")
    print(f"1   {tab[1][0]} | {tab[1][1]} | {tab[1][2]} ")
    print(f"   ___|___|___")
    print(f"      |   |   ")
    print(f"2   {tab[2][0]} | {tab[2][1]} | {tab[2][2]} ")
    print(f"      |   |   \n\n")

def jogar(p_jogador, letra):
    x = 0
    while (x == 0):
        print(f"{p_jogador}, informe a linha e a coluna da jogada:")

        linha = int(input("Linha: "))

        coluna = int(input("Coluna: "))

        x = validador(linha, coluna)

    tab[linha][coluna] = letra

    mostra_velha();	

    check = vencedor()
    if (check == 1):
        print(f"{p_jogador} venceu o jogo.")
        return 1
    else:
        return 0

jogadorx = input("Informe o nome do jogador 1 (X): ")
jogadoro = input("Informe o nome do jogador 2 (O): ")

mostra_velha()

for cont in range(5):

    check = jogar(jogadorx, 'X')

    if (cont == 4 or check == 1):
        break
    
    check = jogar(jogadoro, 'O')

    if (check == 1):
        break

if (check == 0):
    print("O jogo empatou.")