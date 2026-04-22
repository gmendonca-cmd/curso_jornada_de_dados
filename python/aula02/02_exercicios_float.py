# #### Números de Ponto Flutuante (`float`)

#6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_um = float(input("Escreva um número para ser somado: "))
numero_dois = float(input("Agora o outro: "))
soma = numero_um + numero_dois

print(f"{numero_um} + {numero_dois}: {soma}")

#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_tres = float(input("Escreva a nota da 1ª prova: "))
numero_quatro = float(input("Agora a da 2ª prova: "))
media = (numero_tres + numero_quatro) / 2

print(f"A média da suas notas foi de: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_base = float(input("Escreva qualquer número: "))
numero_expoente = float(input("Agora o expoente para eleva-lo: "))

potencia = numero_base ** numero_expoente

print(f"{numero_base} elevado a {numero_expoente} é igual a {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celcius = float(input("Qual a temperatura em local em Celcius? "))

fahrenheit = (celcius * 1.8) + 32

print(f"{celcius}ºC em fahrenheit é {fahrenheit}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
PI = 3.14
raio = float(input("Digite o valor do raio do circulo: "))

area_circulo = PI * raio**2

print(f"A Área do circulo é de {area_circulo}m²")