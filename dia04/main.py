## Exercícios de Listas e Dicionários

### 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
list_numeros: list = list(range(1,11))

for num in list_numeros:
    num_quadrado: int = num ** 2
    print(f"- {num} ao quadrado = {num_quadrado}")

### 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista_linguagens: list = ["Python", "Java", "C++", "JavaScript"]

lista_linguagens.remove("C++")
lista_linguagens.append("Ruby")

print(lista_linguagens)

### 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação.
### Imprima cada informação.
dict_livros: dict = {}
dict_livros_keys: list = ["Título","Autor","Ano"]

while True:
    titulo: str = input("Insira o título do livro: ").strip()

    if titulo == "":
        print("O título do livro não pode estar em branco!")
    elif len(titulo) < 5:
        print("Insira um título válido")
    elif titulo.isnumeric():
        print("O título precisa ter algum caracter!")
    else:
        dict_livros[dict_livros_keys[0]] = titulo
        break

while True:
    autor: str = input("Insira o autor do livro: ").strip()

    if any(caracter.isnumeric() for caracter in autor):
        print("O nome do autor não pode conter números!")
    else:
        dict_livros[dict_livros_keys[1]] = autor
        break

while True:
    try:
        ano_publicacao: int = int(input("Insira o ano de publicação do livro: "))
        dict_livros[dict_livros_keys[2]] = ano_publicacao
        break
    except ValueError:
        print("Insira apenas números no ano de publicação do livro!")

print("\nAs informações do livro inserido foram:")
for key, value in dict_livros.items():
    print(f"- {key}: {value}")

### 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
while True:
    string: str = input("Digite uma string qualquer: ").lower().strip()

    if all(caracter.isalpha() or caracter.isspace() for caracter in string):
        string_sem_espacos: str = string.replace(" ","")
        dict_caracteres: dict = {}

        for caracter in string_sem_espacos:
            if caracter in dict_caracteres:
                dict_caracteres[caracter] += 1
            else:
                dict_caracteres[caracter] = 1

        for caracter, valor in dict_caracteres.items():
            print(f"- O caracter '{caracter}' aparece {valor} vez(es).")
        break
    else:
        print("Insira apenas caracteres!")

### 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
### calcule o preço total da lista de compras.

list_produtos: list = ["maçã", "banana", "cereja"]
dict_produtos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

valor: float = 0

for key in list_produtos:
    valor += dict_produtos.get(key)

print(f"O valor total da lita de compras é igual a: R${valor}")