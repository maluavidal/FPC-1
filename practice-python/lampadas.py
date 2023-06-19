switch_flicked = int(input())
flicks = [int(n) for n in input().split()]

s1_counter = 0
s2_counter = 0

for switch in flicks:
    s1_counter += 1
    if switch == 2:
        s2_counter += 1

def check_if_on(counter):
    if counter % 2 == 0:
        return(0)
    else: return(1)

print(check_if_on(s1_counter))
print(check_if_on(s2_counter))

#   Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem
# duas lâmpadas. Vamos chamá-las de A e B. No hotel há dois interruptores, que chamaremos de I1
# e I2. Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver apagada e apaga se
# estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado.

#   As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você.
# Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado
# final das lâmpadas A e B.

# Entrada
#   A primeira linha contém um número N que representa quantas vezes seu amigo irá apertar algum
# interruptor. Na linha seguinte seguirão N números, que pode ser 1, se o interruptor I1 foi apertado,
# ou 2, se o interruptor I2 foi apertado.

# Saída
#   Seu programa deve imprimir dois valores, em linhas separadas.
# Na primeira linha, imprima 1 se a lâmpada A estiver acesa no final das operações e 0 caso contrário.
# Na segunda linha, imprima 1 se a lâmpada B estiver acesa no final das operações e 0 caso contrário.

# Restrições
# • 1 ≤ N ≤ 105