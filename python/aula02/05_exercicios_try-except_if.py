# #### try-except e if

# 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura 
# em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em
# Fahrenheit ou uma mensagem de erro se a entrada não for válida

try:
     celcius = float(input("Qual a temperatura em local em Celcius? "))   
     fahrenheit = (celcius * 1.8) + 32
     print(f"{celcius}ºC em fahrenheit é {fahrenheit}ºF")
except ValueError:
     print("Por favor, insira um valor numerico")
    
# 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando 
# espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para
# verificar o tipo da entrada.

sentence = input("Digite qualquer palavra: ")

if isinstance(sentence,str):
     sentence = sentence.lower().strip()
     polindromo = sentence[::-1]
    
     if sentence == polindromo:
         print("Sua palavra é um políndromo")
     else:
         print(f"Sua palavra não é um políndromo. Palavra original -> {sentence}, Invertida: {polindromo}")
else:
     print("Entrada Invalida. Por Favor, digite novamente")


# 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except 
# para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no
# operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.


try:
    entrada_um = float(input("Digite o 1º número a ser calculado: "))
    sinal = input("Informe qual é a operação desejada (|+|, |-|, |*|, |/|): ")
    entrada_dois = float(input("Digite o 2° número a ser calculado: "))

    if sinal == "+":
            operacao = entrada_um + entrada_dois
    elif sinal == "-":
            operacao = entrada_um - entrada_dois
    elif sinal == "*":
            operacao = entrada_um * entrada_dois
    elif sinal == "/":
            operacao = entrada_um / entrada_dois
    print(f"{entrada_um} {sinal} {entrada_dois} = {operacao}")              # else:
                                                                            #     # Se cair aqui, o operador é inválido
                                                                            #     operacao = None
                                                                            #     print("Operador inválido!")

                                                                            # # Só imprime se a operação foi realizada com sucesso
                                                                            # if operacao is not None:
                                                                            #     print(f"{entrada_um} {sinal} {entrada_dois} = {operacao}")
except NameError:
        print("Por favor, verifique se está digitando um operador valído")     
except ValueError:
    print("Por favor, verifique se está digitando apenas números")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0")


# 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja 
# numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se
# o número é "par" ou "ímpar".

try:
    numero = float(input("Por favor, digite um número: "))

    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    
    #verificando se é par ou impar 
    if numero % 2 == 0:
        print("É um número par")
    else:
        print("É um número impar")
except:
      print("Por favor, digite um número válido")

# 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de 
# entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento
# da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a
# conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

try:
    lista = input("Digite uma lista de números separados por vírgula: ")
    lista_clear = lista.strip().split(",")
    lista_clear = [int(x) for x in lista_clear]
except ValueError: 
    print("Por favor, digite apenas números inteiros")
else:
    print(lista_clear)

# CORRECAO DO PROFESSOR
# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")