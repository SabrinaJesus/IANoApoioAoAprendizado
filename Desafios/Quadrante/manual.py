# Complexidade: 6

while 1:
    entrada = input()

    separado = entrada.split()

    x = int(separado[0])
    y = int(separado[1])

    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')
    else:
        break