# Complexidade: 1
entrada1 = input()
entrada2 = input()

x1, y1 = map(float, entrada1.split())
x2, y2 = map(float, entrada2.split())

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)

print("{:.4f}".format(distancia))
