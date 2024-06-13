# Complexidade: 2

entrada = float(input())

isencao_1 = 2000 * .08

isencao_2 = 3000 * .18 - (isencao_1)

isencao_3 = 4500 * .28 - (isencao_2)

imposto_acumulado = 0

imposto_acumulado += min(entrada - 2000, 1000) * .08

imposto_acumulado += max(min(entrada - 3000, 1500), 0) * .18

imposto_acumulado += max(entrada - 4500, 0) * .28

if imposto_acumulado <= 0:
    print('Isento')
else:
    print(f'R$ {imposto_acumulado:.2f}')