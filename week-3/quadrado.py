square_dimension = int(input()) # dimensão da matriz quadrada
square = [None] * square_dimension 

for line in range(square_dimension): # criação de lista contendo listas das linhas
    new_line = [int(i) for i in input().split()]
    square[line] = new_line

columns_sum = [0] * square_dimension # inicialização da lista de somas de coluna

# inicializando a soma das linhas como 0, somando cada elemento dentro da lista da linha atual para a variável
def sum_lines(line):
    line_sum = 0 
    for n in range(len(line)):
        line_sum += line[n]

        columns_sum[n] += line[n]

    return line_sum

lines_sum = []

# criando lista que contém cada soma de linha feita a partir da função sum_lines
for i in range(square_dimension):
    if i > square_dimension: break
    lines_sum.append(sum_lines(square[i]))

# inicialização das variáveis necessárias para encontrar o número incorreto dentro da matriz (coluna)
first_column = columns_sum[0]
correct_column = 0
column_error = 0
error_qtd = 0

# compara-se as somas das colunas a partir do índice 1 com a soma encontrada no índice 0, caso sejam diferentes, o erro pode ser encontrado
# no índice daquela coluna, contabilizando esse erro
for i in range(1, square_dimension):
    if (columns_sum[i] != first_column):
        column_error = i
        error_qtd += 1

# caso a diferença entre somas seja encontrada mais de uma vez, então a soma incorreta pode ser encontrada está na primeira coluna, portanto
# no índice 0, sendo assim, um exemplo de coluna correta seria a de índice 1
if (error_qtd > 1):
    column_error = 0
    correct_column = 1

# inicialização das variáveis necessárias para encontrar o número incorreto dentro da matriz (linha)
first_line = lines_sum[0]
correct_line = 0
line_error = 0
error_qtd = 0

# compara-se as somas das linhas a partir do índice 1 com a soma encontrada no índice 0, caso sejam diferentes, o erro pode ser encontrado
# no índice daquela linha, contabilizando esse erro
for i in range(1, square_dimension):
    if (lines_sum[i] != first_line):
        line_error = i
        error_qtd += 1

# caso a diferença entre somas seja encontrada mais de uma vez, então a soma incorreta pode ser encontrada está na primeira linha, portanto
# no índice 0, sendo assim, um exemplo de linha correta seria a de índice 1
if (error_qtd > 1):
    line_error = 0
    correct_line = 1

# ao encontrar o número errado, diminui-se dele a diferença entre a soma das linhas menos a soma das colunas, assim descobrindo o número
# original da matriz quase quadrada, além do próprio número errado a partir da descoberta do índice da linha errada e, dentro dela, com
# o índice da coluna errada, encontra-se o número incorreto da matriz
print(square[line_error][column_error] - (lines_sum[line_error] - columns_sum[correct_column]), square[line_error][column_error])
    