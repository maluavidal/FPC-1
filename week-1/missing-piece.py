total_pieces = range(1, int(input()) + 1)
current_pieces = [int(piece) for piece in input().split()] # list comprehension

def sum(list):
    for piece in list:
        total += piece

# for piece in total_pieces:
#     total_pieces_sum += piece

# for piece_number in current_pieces:
#     current_pieces_sum += piece_number

missing_piece = sum(total_pieces) - sum(current_pieces)

print(missing_piece)