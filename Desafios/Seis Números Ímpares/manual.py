# Complexidade: 3

entrada = int(input())

quantidade_impares = 0

while quantidade_impares < 6:
    if entrada % 2 != 0:
        print(entrada)
        quantidade_impares += 1
    entrada += 1