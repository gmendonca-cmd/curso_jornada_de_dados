## exercicios de fixação

# 1. O Contador Progressivo
# Crie um programa que peça um número ao usuário e, em seguida, imprima todos os números de 1 até esse número (inclusive).

while True: # while usado para repetir se der algum erro
    try:
        numero = int(input("Digite um número: "))
        for i in range(1, numero+1):
            print(i)
        break # quebra o laço pq tudo funcionou corretamente
        
    except ValueError:
        print("Por favor, digite apenas números inteiros") # se nao funcioanr, volta para o inicio 
        



# 2. A Tabuada Dinâmica
# Peça um número ao usuário e use o for para exibir a tabuada desse número (de 1 a 10).
# Exemplo de saída: 5 x 1 = 5, 5 x 2 = 10...

while True: # while usado para repetir se der algum erro
    try:
        produto = int(input("Insira o número para calcular a tabuada: "))
        
        for i in range(1, 11): # 11 - 1 = 10
            tabuada = i * produto
            print(f"{produto} X {i} = {tabuada}")
        break # quebra o laço pq tudo funcionou corretamente
            
    except ValueError:
        print("Por favor, digite apenas números inteiros") # se nao funcioanr, volta para o inicio 




# 3. O Alerta de Pares
# Faça um laço que percorra os números de 1 a 20. Para cada número, o programa deve verificar: se o número for par, imprima "O número [X] é par".
 
for i in range(0, 21): # vai do 1 até o 20
    if i % 2 == 0:
        print(f"O número {i} é par")


# 4. O Somador Acumulativo
# Crie um programa que calcule a soma de todos os números de 1 a 100 e mostre o resultado final.
# Dica: Crie uma variável total = 0 antes do laço e vá somando os números dentro dele.

total = 0 

for i in range(1, 101):
    total += i # vai somando com o número anterior
    print(total)

# 5. Soletrando e Contando
# Peça para o usuário digitar uma palavra (uma string). Use o for para imprimir cada letra da palavra em uma linha diferente.
# Desafio extra: Tente contar quantas letras "a" (ou qualquer outra) existem na palavra usando um if dentro desse for.

while True: # while usado para repetir se der algum erro
    try:
        total = 0
        palavra = input("Digite qualquer palavra: ").lower()
        if any(char.isdigit() for char in palavra):
            raise ValueError("Por favor, digite apenas caracteres") # aqui, forcei um erro se algum número for digitado, e volta novamente para o input 
        else: # se tiver valido com a entrada, o contador e o exibidor de letras ocorre normal
            for i in palavra: # percorre cada letra da palavra
                print(i) # exibe cada letra por vez
                if i == 'a': 
                    total +=1 # se a letra for a, adiciona 1 no contador
            print(f"A letra 'a' aparece {total} vezes")
            break # quebra o laço pq tudo funcionou corretamente
            
    except Exception as e:
        print(e)



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.



### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [1, 2, 5, 7, 10, 12, 14, 17, 22, 23]


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# Measure some strings:


