def sum_list(list):
    s = 0
    for i in list:
        s += i
    return s
# lendo entrada
total_pieces = int(input())
current_pieces = [int(piece) for piece in input().split()] # list comprehension

total_pieces_sum =  int(total_pieces * (total_pieces + 1) / 2)

missing_piece = total_pieces_sum - sum_list(current_pieces)
print(missing_piece)