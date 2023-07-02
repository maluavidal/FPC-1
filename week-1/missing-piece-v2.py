total_pieces = int(input())
current_pieces = [int(piece_number) for piece_number in input().split()]
missing_piece = list(range(1, total_pieces + 1))

for piece in list(range(1, total_pieces + 1)):
    for piece_number in current_pieces:
        if piece == piece_number:
            missing_piece.remove(piece)

print(missing_piece[0])
