def search_highest(balance, start, end):
    highest = balance[start]
    highest_i = start

    for i in range(start, end + 1):
        if balance[i] > highest: 
            highest = balance[i]
            highest_i = i
    return highest_i

n_original_digits, n_removed = [int(i) for i in input().split()]
balance = [int(i) for i in input()]
n_digits = n_original_digits - n_removed
highest_i = -1

for i in range(n_digits):
    start = highest_i + 1
    end = (n_original_digits - 1) - (n_digits - i - 1)
    highest_i = search_highest(balance, start, end)
    print(balance[highest_i], end = "")
