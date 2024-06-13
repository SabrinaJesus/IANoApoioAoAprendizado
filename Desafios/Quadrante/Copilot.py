# Complexidade: 7

while True:
    x, y = map(int, input().split())

    if y == 0:
        break

    if x == 0:
        break

    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 and y < 0:
        print("quarto")