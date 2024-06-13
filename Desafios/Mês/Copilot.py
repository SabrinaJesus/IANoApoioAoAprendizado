# Complexidade: 2

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April", 
    5: "May", 6: "June", 7: "July", 8: "August", 
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Recebe o número do usuário
month_number = int(input())

# Verifica se o número está dentro do intervalo válido
if 1 <= month_number <= 12:
    # Obtém o nome do mês correspondente ao número e imprime com a primeira letra maiúscula
    month_name = month_names[month_number]
    print(month_name)
