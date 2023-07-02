sequence_length = int(input())

marked = 0
current = -1

for _ in range(sequence_length):
    num = int(input())

    if current != num:
        current = num
        marked += 1

print(marked)
