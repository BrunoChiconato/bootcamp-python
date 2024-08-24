# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

string_numeros = input("Forneça uma lista de números separados por ',': ")
string_numeros_formatada = string_numeros.replace(" ","")
lista_numeros_string = string_numeros_formatada.split(",")

lista_numeros_int = []

for num_str in lista_numeros_string:
    try:
        lista_numeros_int.append(int(num_str))
        print(f"Conversão da string '{num_str}' para inteiro foi realizada com sucesso")
    except ValueError:
        print(f"Conversão da string '{num_str}' para inteiro não funcionou, pois '{num_str}' não é um número")

if lista_numeros_int:
    print(f"A lista de números convertida para inteiro é:\n- {lista_numeros_int}")
else:
    print("A lista de números está vazia pois nenhum dado inserido era um número")