p_length1 = int(input())
p_width1 = int(input())
p_length2 = int(input())
p_width2 = int(input())

area1 = p_length1 * p_width1
area2 = p_length2 * p_width2

best_location = area1 if area1 > area2 else area2

print(best_location)

#   Os administradores da Fazenda Fartura planejam criar uma nova plantação de morangos, no formato
# retangular. Eles têm vários locais possíveis para a nova plantação, com diferentes dimensões de
# comprimento e largura. Para os administradores, o melhor local é aquele que tem a maior área.
#   Eles gostariam de ter um programa de computador que, dadas as dimensões de dois locais, determina
# o que tem maior área. Você pode ajudá-los?
# 
# Entrada
#   A entrada contém quatro linhas, cada uma contendo um número inteiro. As duas primeiras linhas
# indicam as dimensões (comprimento e largura) de um dos possíveis locais. As duas últimas linhas
# indicam as dimensões (comprimento e largura) de um outro possível local para a plantação de
# morangos. As dimensões são dadas em metros.
# 
# Saída
#   Seu programa deve escrever uma linha contendo um único inteiro, a área, em metros quadrados, do
# melhor local para a plantação, entre os dois locais dados na entrada.
# 
# Restrições
# • 1 ≤ comprimento ≤ 100
# • 1 ≤ largura ≤ 100