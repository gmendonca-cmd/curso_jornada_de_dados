# Exercício 01
# crie programa que o usuário digita o seu nome e retorna o número de caracteres

nome = input("Qual o seu nome? ")
total = len(nome)
print("O seu nome tem", total, "letras")

# ou -> print(len(input("Qual o seu nome? ")))

# exercicio 2
# Criar um programa onde o usuário digite dois valores e apareça a soma

valorUm = float(input("Qual o primeiro número? "))
ValorDois = float(input("Qual o segundo número? "))
print(f"A soma é: {valorUm+ValorDois}")

