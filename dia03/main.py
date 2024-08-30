### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
condicao = False

while not condicao:
    try:
        quantidade = int(input("Informe a quantidade de vendas de um produto: "))
        preco = float(input("Informe o valor total de vendas do mesmo produto: "))
        condicao = True
    except ValueError:
        print("Insira apenas números")
    
if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
condicao = False

while not condicao:
    try:
        temperatura = float(input("Informe a temperatura do sensor: "))
        condicao = True
    except ValueError:
        print("Insira apenas números")

if temperatura < 18:
    print("A temperatura está baixa")
elif temperatura >= 18 and temperatura <= 26:
    print("A temperatura está normal")
else:
    print("A temperatura está alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
condicao = True
lista_dict = []

keys = ["timestamp", "level", "message"]

while condicao:
    novo_dict = {}

    for key in keys:
        value = input(f"Insira o valor para {key}: ")
        novo_dict[key] = value

    lista_dict.append(novo_dict)

    resposta = input("Deseja inserir mais logs? (S/N): ")
    if resposta.upper() == "N":
        condicao = False
    elif resposta.upper() != "S":
        print("Insira apenas 'S' ou 'N'")

for i, log in enumerate(lista_dict):
    if log.get("level") == "ERROR":
        print(f"Houve um erro no {i+1}º log: {log.get("message")}")

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
condicao = True

while condicao:
    try:
        idade = int(input("Insira sua idade: "))
        email = input("Insira um e-mail válido: ").strip()

        if idade < 18 or idade > 65:
            print("Idade menor que 18 ou acima de 65.")
        elif not email:
            print("O campo 'e-mail' não pode estar vazio.")
        elif any(char.isspace() for char in email):
            print("Não insira espaços no campo 'e-mail'.")
        elif "@" not in email or "." not in email:
            print("O e-mail digitado no campo 'e-mail' precisa ser válido.")
        else:
            condicao = False
            print("Dados de usuário válidos")
    except ValueError:
        print("Insira apenas números no campo 'idade'.")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
condicao = True
list_dict_transacao = []
keys = ["valor", "hora"]

while condicao:
    dict_transacao = {}

    for key in keys:
        value = input(f"Informe o valor para o campo '{key}': ")

        if value.isdigit():
            dict_transacao[key] = value
        else:
            print("Insira apenas valores numéricos!")
            break

    if len(dict_transacao) == len(keys):
        list_dict_transacao.append(dict_transacao)

    resposta = input("Deseja inserir mais transações? (S/N): ")
    if resposta.upper() == "N":
        condicao = False
    elif resposta.upper() != "S":
        print("Insira apenas 'S' ou 'N'")

for i, trans in enumerate(list_dict_transacao):
    valor = float(trans.get("valor"))
    hora = int(trans.get("hora"))

    if valor > 10000:
        print(f"Sua {i+1}ª transação é suspeita, pois o valor a ser transferido foi de: R$ {valor}")
    elif hora < 9 or hora > 18:
        print(f"Sua {i+1}ª transação é suspeita, pois a hora da transferência foi às: {hora}h")  

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
import re

texto = input("Digite um texto: ").strip()

texto_limpo = re.sub(r'[^A-Za-z0-9áéíóúàèìòùâêîôûãõñçÇ ]+', '', texto)

palavras = texto_limpo.split()

contagem_palavras = {}

for palavra in palavras:
    palavra = palavra.lower()
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

for palavra, contagem in contagem_palavras.items():
    if contagem_palavras.get(palavra) == 1:
        print(f"'{palavra}': {contagem}")

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
lista_numeros = []
condicao = True

while condicao:
    try:
        numero = float(input("Forneça um número: "))
        lista_numeros.append(numero)

        while condicao:
            resposta = input("Deseja inserir mais números? (S/N): ").upper()

            if resposta == "N":
                condicao = False
                break
            elif resposta == "S":
                break
            else:
                print("Resposta inválida. Insira apenas 'S' para continuar ou 'N' para parar.")

        if not condicao:
            break

    except ValueError:
        print("Insira apenas números!")

print(f"Lista fornecida: {lista_numeros}")

numeros_pares = [num for num in lista_numeros if num % 2 == 0]

if numeros_pares:
    print("Números pares dentro da lista fornecida:")
    for num in numeros_pares:
        print(f"- {num}")
else:
    print("Sem números pares na lista fornecida")

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
condicao = True
vendas = []
keys = ["Categoria","Venda"]

while condicao:
    dict_vendas = {}

    while True:
        categoria = input("Insira a categoria da venda: ").upper()

        if not categoria.isalpha():
            print("Insira apenas caracteres no campo 'categoria'!")
        else:
            dict_vendas[keys[0]] = categoria
            break

    while True:
        try:
            venda = float(input("Insira o valor da venda: "))
            dict_vendas[keys[1]] = venda
            break
        except ValueError:
            print("Insira apenas valores para o campo 'venda'!")

    vendas.append(dict_vendas)

    while True:
        resposta = input("Deseja inserir mais registros de vendas? (S/N): ").upper()
        
        if resposta == "N":
            condicao = False
            break
        if resposta == "S":
            break
        else:
            print("Insira apenas 'S' ou 'N'")

total_vendas_por_categoria = {}

for venda in vendas:
    categoria = venda["Categoria"]
    valor = venda["Venda"]
    
    if categoria in total_vendas_por_categoria:
        total_vendas_por_categoria[categoria] += valor
    else:
        total_vendas_por_categoria[categoria] = valor

print("\nTotal de vendas por categoria:")
for categoria, total in total_vendas_por_categoria.items():
    print(f"{categoria}: R${total:.2f}")

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
condicao = True
keys = ["dado"]
list_dict_dados = []

while condicao:
    dict_dados = {}
    for key in keys:
        dict_dados[key] = input("Insira um dado (digite 'sair' para parar de fornecer dados): ")

        if dict_dados.get(key).lower() == "sair":
            condicao = False
            break
        else:
            list_dict_dados.append(dict_dados)

if list_dict_dados:
    print("Os dados de entrada foram:")
    for dict_dados in list_dict_dados:
        for value in dict_dados.values():
            print(f"- {value}")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
condicao = True
intervalo_comparacao = [5, 100]

min_intervalo = intervalo_comparacao[0] 
max_intervalo = intervalo_comparacao[1]

while condicao:
    try:
        numero = float(input(f"Insira um número entre {min_intervalo} e {max_intervalo}: "))

        if numero > min_intervalo and numero < max_intervalo:
            print("Entrada válida!")
            condicao = False
        else:
            print("Insira um número dentro do intervalo fornecido!")
    except ValueError:
        print("Insira apenas números!")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
