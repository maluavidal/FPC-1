def busca_maior(saldo, inicio, fim):
    maior = saldo[inicio]
    maior_idx = inicio

    for i in range(inicio, fim + 1):
        if saldo[i] > maior: 
            maior = saldo[i]
            maior_idx = i
    return maior_idx

n_digitos_original, n_removidos = [int(i) for i in input().split()]
saldo = [int(i) for i in input()]
n_digitos = n_digitos_original - n_removidos
maior_idx = -1

for i in range(n_digitos):
    inicio = maior_idx + 1
    fim = (n_digitos_original - 1) - (n_digitos - i - 1)
    maior_idx = busca_maior(saldo, inicio, fim)
    print(saldo[maior_idx], end = "")
