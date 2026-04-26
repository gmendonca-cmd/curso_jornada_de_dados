## Refatore o código do desafio 1 usando try-except para cobrir todos os possíveis erros

NUMERO_CONSTANTE = 1000 # variaves maisculas são variaveis consantes (nao mutaveis) em python

try:
    nome = input("Insira o seu nome: ")
    if len(nome) == 0:
        raise ValueError("Nome não pode estar vazio") # raise é usado para forçamos o erro, logo em seguida, especificamos o erro
    elif any(char.isdigit() for char in nome): # usado pra descobrir se existe número no input
        raise ValueError("Nome não pode conter números") 
    else:
        print("Nome Válido")
except ValueError as e:  # faz exibir o tipo de erro
    print(e)

try:
    salario = float(input("Digite o seu salário: "))
    if salario < 0:
        raise ValueError("O salário não pode ser negativo")
except ValueError:
    print("Verifique se há apenas números")

try:
    bonus = float(input("Digite o valor do bônus. Ex: 1.5 (50%): "))
    if bonus < 0:
        raise ValueError("O valor do bônus não pode ser negativo")
except ValueError:
    print("Verifique se há apenas números")


kpi = (NUMERO_CONSTANTE + salario) * bonus

print(f"Olá {nome}, o seu valor bônus foi de R${kpi}")