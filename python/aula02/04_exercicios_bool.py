# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND
# entre elas.
preposicao1 = input("A 1ª preposição é True ou False? ")
preposicao2 = input("A 2ª preposição é True ou False? ")
resultado_and = preposicao1 and preposicao2

print(f"O resultado do operador lógico and, neste caso é: {resultado_and}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
preposicao3 = input("A 1ª preposição é True ou False? ")
preposicao4 = input("A 2ª preposição é True ou False? ")
resultado_or = preposicao3 or preposicao4

print(f"O resultado do operador lógico or, neste caso é: {resultado_or}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
preposicao5 = input("A preposição é True ou False? ")
resultado_not = not preposicao5

print(f'O resultado da preposição utilizando o operador not, neste caso, é: {resultado_not}')

# 19. Faça um programa que compare se dois números fornecidos pelusuário são iguais.
numero_1 = float(input("Digite um número:"))
numero_2 = float(input("Digite outro número:"))
resultado_igual = (numero_1 == numero_2)

print(f"Os dois números são iguais? {resultado_igual}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero_3 = float(input("Digite um número:"))
numero_4 = float(input("Digite outro número:"))
resultado_diferente = (numero_3 != numero_4)

print(f"Os dois números são diferentes? {resultado_diferente}")