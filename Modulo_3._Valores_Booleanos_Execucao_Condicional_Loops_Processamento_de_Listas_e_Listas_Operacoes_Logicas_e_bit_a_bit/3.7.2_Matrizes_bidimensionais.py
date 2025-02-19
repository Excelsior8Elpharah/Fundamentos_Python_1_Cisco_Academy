# Cenário
# Vamos supor também que um símbolo predefinido chamado EMPTY designa um campo vazio no tabuleiro.
# Então, se queremos criar uma lista de listas representando todo o tabuleiro de xadrez, isso pode ser feito da seguinte maneira:

EMPTY = " "  # Símbolo para campo vazio
ROOK = "R"    # Torre
KNIGHT = "N"  # Cavaleiro
PAWN = "P"    # Peão

# Criar o tabuleiro 8x8 com campos vazios (EMPTY)
board = [[EMPTY for i in range(8)] for j in range(8)]

# Colocar as torres nas posições iniciais
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

# Colocar o cavaleiro na posição C4 (índice [4][2])
board[4][2] = KNIGHT

# Colocar um peão na posição E5 (índice [3][4])
board[3][4] = PAWN

# Imprimir o tabuleiro para visualização
for row in board:
    print(row)