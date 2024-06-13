# Complexidade: 1

entrada1 = input()
entrada2 = input()


x1, y1 = entrada1.split()
x2, y2 = entrada2.split()

x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** .5

print("{:.4f}".format(distancia))
