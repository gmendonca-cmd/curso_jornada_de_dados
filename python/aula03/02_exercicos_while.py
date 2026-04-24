# i = 0
# while i <= 10: 
#     print(i)
#     i += 1 # para acrescentar 1 a cada vez que passa no laço. só vai parar quando i for maior que 10  


### exercicios de fixação 
# 1. Você está criando um sistema que pede uma senha para o usuário.
# Você quer que o programa continue pedindo a senha enquanto o que ele digitar for diferente da senha correta.

# try:
#     senha = input("Por favor, digite sua senha: ")
    
#     while senha != "python123":
#         print("Senha incorreta")
#         senha = input("Por favor, digite a senha novamente: ")
#     print("Acesso liberado")

# except: 
#     print("Erro ao digitar a senha")


# 02. Imagine que você recebeu uma caixa com várias frutas (um número que o usuário vai digitar). Você precisa "processar" cada fruta, uma por uma, exibindo na 
# tela: "Processando fruta número 1", "Processando fruta número 2", até chegar ao total.
# Dica: Você vai precisar de uma variável para contar em qual fruta você está.



i = 1

while True:
    try:
        frutas = int(input("Digite quantas frutas tem na caixa: "))
        break
    except ValueError:
        print("Por favor, digite apenas números")
    
while i <= frutas:
    print(f"Processando fruta número {i}")
    i += 1    


# 03. Um professor quer somar as notas dos alunos, mas ele não sabe quantos alunos vieram hoje. Crie um programa que peça a nota do aluno. O programa deve 
# continuar pedindo notas enquanto o professor não digitar o número -1. No final, mostre a soma total das notas digitadas.
# Dica: O -1 aqui funciona como um "Sinal de Parada" (conhecido na programação como Sentinela).

notas = 0
total = 0
while notas != -1: # vai continuar até colocar a ordem de parada (-1)
    try:   
        notas = float(input("Digite a nota: "))
            
        if notas >= 0: # se a nota for maior ou igual a 0, somar as notas
            total = total + notas
        else:
            print("Por favor, digite um nova igual ou maior que 0") # se for uma nota negativa, ela não é adicionada e o programa pede uma nova nota
    except ValueError:
        print("Por favor, digite apenas números")

print(f"O total das notas é: {total}")



# 04. Uma empresa de logística tem um estoque de 100 pacotes. A cada ciclo, alguns pacotes são despachados (o usuário diz quantos). Crie um programa que subtraia 
# os pacotes do estoque enquanto o estoque for maior que 10. Quando atingir 10 ou menos, o programa para e avisa: "Alerta: Estoque crítico! Reposição necessária."



estoque = 100
while estoque >= 11:
    try:
        retirada = int(input(f"Estoque atual: {estoque}. Digite aqui quantos pacotes você quer retirar: "))
            
        if retirada <= estoque:
            estoque -= retirada
        else:
            print("Valor superior ao estoque disponível")
            
    except ValueError:
        print("Por favor, digite um valor válido")

print(f"Alerta: Estoque crítico!({estoque}) Reposição necessária")




### Exercícios com WHILE do jornada

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.