# Complexidade: 7

salario = float(input())

if salario < 0:
    print('Salário não pode ser negativo')
if salario <= 400.00:
    percentual = 15
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
elif salario <= 800.00:
    percentual = 12
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
elif salario <= 1200.00:
    percentual = 10
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
elif salario <= 2000.00:
    percentual = 7
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
else:
    percentual = 4
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))
