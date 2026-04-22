# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
upper = input("Escreva qualquer coisa: ")
string_maiuscula = upper.upper()
print(string_maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_lower = input("Escreva seu nome completo: ")
nome_minusculo = nome_lower.lower()
print(nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco
# no início e no final.
frase_strip = input("Digite uma frase:")
frase_sem_espacos = frase_strip.strip()
print(f"Frase sem espaços no meio e fim: {frase_sem_espacos}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e
# o ano separadamente.
data_split = input("Digite uma data qualquer no formato dd/mm/aaaa: ")
data_separada = data_split.split("/")
print(data_separada)

print(f'Dia: {data_separada[0]}')
print(f'Mês: {data_separada[1]}')
print(f'Ano: {data_separada[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
primeiro_nome = input("Escreva seu primeiro nome:")
ulitmo_nome = input("Escreva seu último nome: ")
nome_completo = primeiro_nome + ulitmo_nome

print(f'Seja bem-vindo Sr(a) {nome_completo}')