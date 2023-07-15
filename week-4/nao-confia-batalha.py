n_rows, n_columns = [int(i) for i in input().split()] #são recebidas as quantidades de linhas e colunas do tabuleiro
board = [None] * n_rows #o tabuleiro é inicializado em forma de matriz

for line in range(n_rows): #incrementa-se uma linha a cada laço de acordo com o input de linhas
    board[line] = [char for char in input()]

def search_ship(board, coord_row, coord_col, ship_number):
    if board[coord_row][coord_col] == '#': #verificando se há um navio, ou parte dele, na coordenada recebida
        board[coord_row][coord_col] = ship_number 
        ships[ship_number] += 1 #guarda-se então as quantidades das partes do navio encontrado
    else:
        return
    #verificando se o navio possui mais partes ao checar as coordenadas vizinhas a ele
    if coord_row - 1 >= 0:
        search_ship(board, coord_row - 1, coord_col, ship_number)
    if coord_col - 1 >= 0:
        search_ship(board, coord_row, coord_col - 1, ship_number)
    if coord_row + 1 < n_rows:
        search_ship(board, coord_row + 1, coord_col, ship_number)
    if coord_col + 1 < n_columns:
        search_ship(board, coord_row, coord_col + 1, ship_number)

ships = []
ship_number = 0

for i in range(n_rows): #percorre-se o tabuleiro
    for j in range(n_columns):
        if board[i][j] == '#': #se um navio for encontrado, adiciona-se uma nova 'casa' a ships, para ser incrementado posteriormente caso o navio tenha mais de uma parte
            ships.append(int(0))
            search_ship(board, i, j, ship_number)
            ship_number += 1

n_shots = int(input()) #quantidade de disparos recebidos

for _ in range(n_shots): 
    row_shot, col_shot = [int(i) for i in input().split()] #recebendo as coordenadas dos disparos
    try:
        shot_coord = int(board[row_shot - 1][col_shot - 1]) #-1 para que o recebido no input de linhas e colunas seja compatível aos índices utilizados nas coordenadas
        ships[shot_coord] -= 1 #quando a coordenada do navio é igual a do disparo recebido, remove-se uma parte dele
    except:
        continue

destroyed_ships = 0

for ship in ships: #verificando a quantidade de navios que foi destruída
    if ship == 0: #se o navio agora tem 0 partes, então ele foi destruído
        destroyed_ships += 1

print(destroyed_ships)
