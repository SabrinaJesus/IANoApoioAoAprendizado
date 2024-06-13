# Complexidade: 6

entrada = float(input())

if entrada <= 400.00:
    percentual = 15
    reajuste = entrada * (percentual / 100)
    salario_reajustado = entrada + reajuste
elif entrada <= 800.00:
    percentual = 12
    reajuste = entrada * (percentual / 100)
    salario_reajustado = entrada + reajuste
elif entrada <= 1200.00:
    percentual = 10
    reajuste = entrada * (percentual / 100)
    salario_reajustado = entrada + reajuste
elif entrada <= 2000.00:
    percentual = 7
    reajuste = entrada * (percentual / 100)
    salario_reajustado = entrada + reajuste
else:
    percentual = 4
    reajuste = entrada * (percentual / 100)
    salario_reajustado = entrada + reajuste

print(f"Novo salario: {salario_reajustado:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
