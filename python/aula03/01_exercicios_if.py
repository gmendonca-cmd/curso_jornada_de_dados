### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

try:
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o valor: "))
    
    if quantidade >= 0 and preco >= 0:
        print("Dados Válidos")
    else:
        print("Dados Inválidos")

except: print("Verifique se está digitando apenas números")



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


try:
    temperatura = float(input("Insira a temperatura em °C: "))

    if temperatura > 26:
        print("Temperatura Alta")
    elif temperatura >= 18 and temperatura <= 26:
        print("Temperatura Normal")
    else:
        print("Temperatura Baixa")
except: 
    print("Digite uma temperatura válida")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'OK', 'message': 'Falha na conexão'}

try:
    verificacao = log['level']
    if verificacao == "ERROR":
        print(log['message'])
except KeyError as e:
    print(e) 



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.


try:
    idade = int(input("Digite sua idade: "))
    

    if not (18 <= idade <= 65) :
        print("Idade fora do requisito")
    else: 
        email = input('Digite seu email: ')
        if ("@" not in email or "." not in email):
            print("Por favor, digite um email válido")
        else:
            print("Dados Válidos")
except ValueError:  
    print("Por favor, digite um idade válida")
 






### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 10000,
             'hora': 18}

try:
    verificacao_valor = transacao['valor']
    verificacao_hora = transacao['hora']
    
    if verificacao_valor > 10000 or (verificacao_hora < 9 or verificacao_hora > 18):
        print("Transação Suspeita")
    else:
        print("Transação normal") 
except KeyError as e:
    print(f"O campo {e} está faltando na transação")
except TypeError:
    print("Os dados da transação não são números válidos")
