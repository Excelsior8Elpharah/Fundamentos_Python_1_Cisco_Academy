from random import randrange

# Cenário
# Sua tarefa é escrever um programa simples que finge jogar tic-tac-toe com o usuário.
# Para tornar tudo mais fácil para você, decidimos simplificar o jogo. Aqui estão nossas suposições:
# - O computador (ou seja, seu programa) deve jogar usando 'X's;
# - O usuário (por exemplo, você) deve jogar usando 'O's;
# - O primeiro movimento pertence ao computador - ele sempre coloca seu primeiro 'X' no meio do quadro;
# - Todos os quadrados são numerados linha por linha, começando com 1;
# - O usuário insere seu movimento inserindo o número do quadrado escolhido;
# - O programa verifica se o jogo acabou - quatro veredictos possíveis: continuar, empate, você ganha ou o computador ganha;
# - O computador responde seu movimento e a verificação é repetida;
# - Não implementamos qualquer forma de inteligência artificial - uma escolha de campo aleatória feita pelo computador é suficiente.

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    ok = False
    while not ok:
        move = input("Digite seu movimento: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Má jogada – repita sua entrada!")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['O','X']
        if not ok:
            print("Campo já ocupado – repita sua entrada!")
            continue
    board[row][col] = 'O'

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                free.append((row,col))
    return free

def victory_for(board, sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor is not None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")