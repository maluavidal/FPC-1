def createCombinations(elements, k):
    if k == 0:
        return [[]]

    elements_length = 0
    for _ in elements:
        elements_length += 1

    if not elements or k > elements_length:
        return []

    first = elements[0]
    rest = elements[1:]

    combinations_without_first = createCombinations(rest, k)
    combinations_with_first = [[first] + c for c in createCombinations(rest, k-1)]

    return combinations_without_first + combinations_with_first


n = 60  # Número total de elementos disponíveis
k = 6   # Número de elementos das combinações na mega-sena

numbers = list(range(1, n+1))

combinations = createCombinations(numbers, k)

# Imprimir as combinações
for combination in combinations:
    print(combination)