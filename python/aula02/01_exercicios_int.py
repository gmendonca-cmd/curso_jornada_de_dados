# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_um = int(input("Escreva um número para ser somado: "))
numero_dois = int(input("Agora o outro: "))
soma = numero_um + numero_dois

print(f"{numero_um} + {numero_dois}: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_divisao = int(input("Escreva qualquer número: "))
resto = numero_divisao % 5

print(f"O resto desse número divido por 5 é: {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_quatro = int(input("Escreva o primeiro número a ser multiplicado: "))
numero_cinco = int(input("Agora escreva o segundo: "))
multiplicacao = numero_um * numero_dois

print(f"{numero_quatro} x {numero_cinco}: {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_seis = int(input("Escreva o número a ser dividido: "))
numero_sete = int(input("Agora o seu divisor: "))
divisao = numero_seis / numero_sete 

print(f"{numero_seis} / {numero_sete}: {divisao}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_quadrado = int(input("Escreva um número a ser elevado ao quadrado: "))
elevado = numero_quadrado ** 2

print(elevado)


