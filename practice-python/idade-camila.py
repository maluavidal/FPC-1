camila = int(input())
cibele = int(input())
celeste = int(input())

youngest = cibele
oldest = camila
if cibele > camila:
    oldest = cibele
    youngest = camila
if celeste < youngest:
    middle_child = youngest
elif celeste > oldest:
    middle_child = oldest
else:
    middle_child = celeste

print(middle_child)

#   Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes,
# ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para
# desenvolverem seus próprios jogos.
#   Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos
# que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.
# Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar
# a idade de Camila.

# Entrada
#   A entrada é composta por três linhas, cada linha contendo um número inteiro N, a idade de uma
# das irmãs.

# Saída
#   Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila.

# Restrições
# • 5 ≤ N ≤ 100