n_linhas = int(input())
quadrado = [None] * n_linhas

for linha in range(n_linhas):
    nova_linha = [int(i) for i in input().split()]
    quadrado[linha] = nova_linha

print(quadrado)
