# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
v1 = int(input("Insira o primeiro valor: "))
v2 = int(input("Insira o segundo valor: "))
soma = v1 + v2
print(f"A soma dos dois números é igual a: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
v1 = int(input("Insira um valor numérico: "))
resto_divisao = v1 % 5
print(f"O resto da divisão de {v1} por 5 é igual a: {resto_divisao}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
v1 = int(input("Insira o primeiro valor: "))
v2 = int(input("Insira o segundo valor: "))
multiplicacao = v1 * v2
print(f"A multiplicação de {v1} por {v2} é igual a: {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
v1 = int(input("Insira o primeiro valor: "))
v2 = int(input("Insira o segundo valor: "))
div_inteira = v1 // v2
print(f"A divisão inteira de {v1} por {v2} é igual a: {div_inteira}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
v1 = int(input("Insira um valor numérico: "))
num_quadrado = v1**2
print(f"{v1} ao quadrado é igual a: {num_quadrado}")

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
v1 = float(input("Insira o primeiro valor: "))
v2 = float(input("Insira o segundo valor: "))
soma = v1 + v2
print(f"A soma de {v1} + {v2} é igual a: {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
v1 = float(input("Insira o primeiro valor: "))
v2 = float(input("Insira o segundo valor: "))
media = (v1 + v2) / 2
print(f"A média de {v1} e {v2} é igual a: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
v1 = float(input("Insira uma base: "))
v2 = float(input("Insira um expoente: "))
exp = v1**v2
print(f"{v1} elevado a {v2} é igual a: {exp}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
v1 = float(input("Insira a temperatura em graus Celsius: "))
conver_celsius_fahr = (v1 * (9 / 5)) + 32
print(f"{v1}ºC é igual a: {conver_celsius_fahr}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
r = float(input("Insira o raio do círculo: "))
area_circulo = 3.1415 * r**2
print(f"A área do círculo de raio {r} é igual a: {area_circulo}")

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = input("Escreva uma string: ")
string_upper = string.upper()
print(f"Sua string com todas as letras em maiúsculo é igual a: {string.upper}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Escreva seu nome: ")
nome_min = nome.lower()
print(f"Seu nome com todas as letras em minúsculo é: {nome_min}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Forneça uma frase: ")
frase_sem_espacos = frase.strip()
print(f"A frase sem espaços em branco é: {frase_sem_espacos}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Insira uma data no formado dd/mm/aaaa: ")
data_separada = data.split("/")
dia = data_separada[0]
mes = data_separada[1]
ano = data_separada[2]
print(f"Dia: {dia}\nMes: {mes}\nAno: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Forneca a primeira string: ")
string2 = input("Forneca a segunda string: ")
string_concat = string1 + string2
print(f"Concatenacao de duas strings: {string_concat}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool1 = input("Insira o primeiro booleano: ")

if bool1 == "True":
    bool1 = True
    bool2 = input("Insira o segundo booleano: ")
    if bool2 == "True":
        bool2 = True
        op_bool = bool1 and bool2
        print(
            f"A operacao 'and' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    elif bool2 == "False":
        bool2 = False
        op_bool = bool1 and bool2
        print(
            f"A operacao 'and' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    else:
        print("Entrada inválida para o segundo booleano digitado")

elif bool1 == "False":
    bool1 = False
    bool2 = input("Insira o segundo booleano: ")
    if bool2 == "True":
        bool2 = True
        op_bool = bool1 and bool2
        print(
            f"A operacao 'and' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    elif bool2 == "False":
        bool2 = False
        op_bool = bool1 and bool2
        print(
            f"A operacao 'and' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    else:
        print("Entrada inválida para o segundo booleano digitado")

else:
    print("Entrada inválida para o primeiro booleano")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
bool1 = input("Insira o primeiro booleano: ")

if bool1 == "True":
    bool1 = True
    bool2 = input("Insira o segundo booleano: ")
    if bool2 == "True":
        bool2 = True
        op_bool = bool1 or bool2
        print(
            f"A operacao 'or' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    elif bool2 == "False":
        bool2 = False
        op_bool = bool1 or bool2
        print(
            f"A operacao 'or' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    else:
        print("Entrada inválida para o segundo booleano digitado")

elif bool1 == "False":
    bool1 = False
    bool2 = input("Insira o segundo booleano: ")
    if bool2 == "True":
        bool2 = True
        op_bool = bool1 or bool2
        print(
            f"A operacao 'or' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    elif bool2 == "False":
        bool2 = False
        op_bool = bool1 or bool2
        print(
            f"A operacao 'or' entre os dois booleanos fornecidos é igual a: {op_bool}"
        )
    else:
        print("Entrada inválida para o segundo booleano digitado")

else:
    print("Entrada inválida para o primeiro booleano")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
bool1 = input("Insira um valor booleano: ")

if bool1 == "True":
    bool1 = False
elif bool1 == "False":
    bool1 = True
else:
    print("Entrada inválida")

print(f"O valor invertido da entrada é igual a: {bool1}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
bool1 = True
bool2 = False
bool_comp = bool1 == bool2

if bool_comp == True:
    print("Os dois booleanos são iguais")
else:
    print("Os dois booleanos são diferentes")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
bool1 = True
bool2 = False
bool_comp = bool1 != bool2

if bool_comp == True:
    print("Os dois booleanos são diferentes")
else:
    print("Os dois booleanos são iguais")

# #### TypeError, Type Check e Type Conversion

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica,
# tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    temp_c = float(input("Insira uma temperatura em graus Celsius: "))
    temp_f = (temp_c * 9 / 5) + 32
    print(f"A temperatura convertida para Fahreinheit é: {temp_f}ºF")
except ValueError:
    print("O valor inserido não é um número")

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente,
# desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
string = input("Insira uma string: ")

if isinstance(string, str):
    string_formatada = string.replace(" ", "").lower()
    if string_formatada == string_formatada[::-1]:
        print("A string fornecida é um palíndromo")
    else:
        print("A string fornecida não é um palíndromo")
else:
    print("Entrada inválida")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação
# matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    num1 = float(input("Insira o primeiro valor: "))
    num2 = float(input("Insira o segundo valor: "))
    operacao = input("Insira um operador: ")

    if operacao == "+":
        resultado = num1 + num2
        print(f"O resultado de {num1} {operacao} {num2} é igual a: {resultado}")
    elif operacao == "-":
        resultado = num1 - num2
        print(f"O resultado de {num1} {operacao} {num2} é igual a: {resultado}")
    elif operacao == "*":
        resultado = num1 * num2
        print(f"O resultado de {num1} {operacao} {num2} é igual a: {resultado}")
    elif operacao == "/":
        resultado = num1 / num2
        print(f"O resultado de {num1} {operacao} {num2} é igual a: {resultado}")
    else:
        print("Insira um operador válido")

except ValueError:
    print("Insira um valor numérico")

except ZeroDivisionError:
    print("Não é possível realizar divisões por zero")

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja
# numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero".
# Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    num = int(input("Insira um número qualquer: "))

    if num > 0:
        if num % 2 == 0:
            print("O número fornecido é positivo e par")
        else:
            print("O número fornecido é positivo e ímpar")
    elif num < 0:
        print("O número fornecido é negativo")
    elif num == 0:
        print("O número fornecido é igual a zero")

except ValueError:
    print("Não é permitido entradas não numéricas")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

string_numeros = input("Forneça uma lista de números separados por ',': ")
string_numeros_formatada = string_numeros.replace(" ", "")
lista_numeros_string = string_numeros_formatada.split(",")

lista_numeros_int = []

for num_str in lista_numeros_string:
    try:
        lista_numeros_int.append(int(num_str))
        print(f"Conversão da string '{num_str}' para inteiro foi realizada com sucesso")
    except ValueError:
        print(
            f"Conversão da string '{num_str}' para inteiro não funcionou, pois '{num_str}' não é um número"
        )

if lista_numeros_int:
    print(f"A lista de números convertida para inteiro é:\n- {lista_numeros_int}")
else:
    print("A lista de números está vazia pois nenhum dado inserido era um número")
