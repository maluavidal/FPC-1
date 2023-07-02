def successorFn(num): # função que retorna o sucessor do número passado
    return num + 1

def sumFn(num1, num2):
    for _ in range(num2): # o range definirá a quantidade de vezes que 1 será somado a num1, incrementando esse valor a cada laço
        num1 = successorFn(num1)
    return num1

def multiplyFn(num1, num2): 
    result = 0 # inicialização da variável para que se possa atribuir seu devido valor posteriormente a partir de 0
    for _ in range(num1): # o range definirá a quantidade de vezes que o valor de num2 será somado ao resultado, representando uma multiplicação
        result = sumFn(result, num2)
    return result

def exponentialFn(num1, num2):
    result = 1 # inicialização da variável para que se num2 = 0, retorne 1, e para que num1 não seja multiplicado por 0 
    for _ in range(num2): # o range de num2 definirá a quantidade de vezes que o valor de num1 será multiplicado por ele mesmo
        result = multiplyFn(result, num1)
    return result

result = []

while True:
    operation = input().split()
    if len(operation) >= 2:
        function = operation[0]
        a = int(operation[1])

    if len(operation) >= 3:
        b = int(operation[2])

    if function == "Suc":
        result.append(successorFn(a))
    if function == "Soma":
        result.append(sumFn(a, b))
    if function == "Mult" or function == "Multi":
        result.append(multiplyFn(a, b))
    if function == "Exp":
        result.append(exponentialFn(a, b))
    if not operation:
        break

results = len(result)
for i in range(results - 1):
    print(result[i])
    