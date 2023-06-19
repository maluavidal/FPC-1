# lendo entrada, declarando variáveis e atribuindo seus valores
x0a, y0a, x1a, y1a =  [int(n) for n in input().split()]
x0b, y0b, x1b, y1b =  [int(n) for n in input().split()]
# verificando se eixos não colidem de acordo com suas coordenadas
if x0b > x1a or x1b < x0a or y0b > y1a or y1b < y0a:
    print(0)
else:
    print(1)