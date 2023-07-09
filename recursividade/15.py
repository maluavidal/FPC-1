# 15) Pode-se calcular o resto da divisão, MOD, de x por y, dois números inteiros positivos, usando-se a definição abaixo.
# Implemente este algoritmo.
# MOD(x,y) = MOD(x - y, y) se x > y
# MOD(x,y) = x se x < y
# MOD(x,y) = 0 se x = y

def mod(x, y):
    if x == y: return 0
    elif x < y: return x
    else: return mod(x - y, y)

print(mod(7, 5))
