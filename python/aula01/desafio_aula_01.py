# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus
# que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em 
# comparação com o bônus recebido.

# O programa deve começar solicitando ao usuário que insira seu nome.
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
NUMERO_CONSTANTE = 1000 # variaves maisculas são variaveis consantes (nao mutaveis) em python

nome = input("Insira o seu nome: ")
salario = float(input("Digite o seu salário: "))
bonus = float(input("Digite o valor do bônus. Ex: 1.5 (50%): "))

kpi = (NUMERO_CONSTANTE + salario) * bonus

print(f"Olá {nome}, o seu valor bônus foi de R${kpi}")