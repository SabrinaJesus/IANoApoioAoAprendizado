# Complexidade: 0

entrada = int(input())

anos = int(entrada / 365)

restante = entrada - (anos * 365)

meses = int(restante / 30) 

restante = restante - (meses * 30)

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{restante} dia(s)')
