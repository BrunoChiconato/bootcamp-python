## Exercícios de Listas e Dicionários

### 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
list_numeros: list = list(range(1, 11))

for num in list_numeros:
    num_quadrado: int = num**2
    print(f"- {num} ao quadrado = {num_quadrado}")

### 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista_linguagens: list = ["Python", "Java", "C++", "JavaScript"]

lista_linguagens.remove("C++")
lista_linguagens.append("Ruby")

print(lista_linguagens)

### 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação.
### Imprima cada informação.
dict_livros: dict = {}
dict_livros_keys: list = ["Título", "Autor", "Ano"]

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
        string_sem_espacos: str = string.replace(" ", "")
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

### 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
lista_original: list = [
    "brunochiconato@example.com",
    "brunochiconato@example.com",
    "lvgalvao@example.com",
    "jornadadedados@example.com",
    "jornadadedados@example.com",
    "python@example.com",
]
lista_unica: list = []

for item in lista_original:
    if item not in lista_unica:
        lista_unica.append(item)

print(lista_unica)

### 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
lista_idades: list = []
lista_idades_filtradas_unicas: list = []

while True:
    try:
        idade: int = int(
            input("Forneça uma idade (digite '0' para parar de inserir): ")
        )
        if idade == 0:
            break
        else:
            lista_idades.append(idade)
    except ValueError:
        print("Insira apenas números!")

for idade in lista_idades:
    if idade not in lista_idades_filtradas_unicas:
        if idade >= 18:
            lista_idades_filtradas_unicas.append(idade)

print("Lista filtrada apenas com idades maiores ou iguais a 18:")
print(sorted(lista_idades_filtradas_unicas))

### 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
lista_pessoas: list = [
    {"Nome": "Bruno", "Idade": 25},
    {"Nome": "Luciano", "Idade": 36},
    {"Nome": "Ana", "Idade": 18},
]

lista_pessoas_ordenadas: list = sorted(
    lista_pessoas, key=lambda lista_pessoas: lista_pessoas["Nome"]
)

print(lista_pessoas_ordenadas)

### 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
lista_dados: list = []

while True:
    while True:
        try:
            dados: float = float(
                input("Insira números (digite '0' para parar de inserir números): ")
            )

            if dados == 0:
                break
            else:
                lista_dados.append(dados)

        except ValueError:
            print("Insira apenas números")

    if not lista_dados:
        print("A lista de dados não possui nenhum dado. Insira dados!")
    else:
        break

media: float = sum(lista_dados) / len(lista_dados)
print(f"A média da lista de dados fornecida é igual a: {media}")

### 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
lista_valores: list = []

while True:
    while True:
        try:
            valores: int = int(
                input("Insira números inteiros. Digite '0' para parar: ")
            )

            if valores == 0:
                break
            else:
                lista_valores.append(valores)

        except ValueError:
            print("Insira apenas números inteiros!")

    if not lista_valores:
        print("Insira algum número!")
    else:
        break

lista_pares: list = [numero for numero in lista_valores if numero % 2 == 0]
lista_impares: list = [numero for numero in lista_valores if numero % 2 != 0]

print(f"Lista de números pares:\n{lista_pares}")
print(f"Lista de números ímpares:\n{lista_impares}")

## Exercícios com Dicionários

### 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
condicao: bool = True
lista_produtos: list = []
lista_keys: list = ["Produto", "Preço"]

while condicao:
    while True:
        dict_produtos: dict = {}
        produto: str = input("Insira o nome do produto: ").strip()

        produto_existe: bool = any(
            item[lista_keys[0]].lower() == produto.lower() for item in lista_produtos
        )

        if produto_existe:
            print("Esse produto já foi adicionado. Por favor, insira outro produto.")
        else:
            break

    if all(caracter.isalpha() or caracter.isspace() for caracter in produto):
        dict_produtos[lista_keys[0]] = produto

        while True:
            try:
                preco: float = float(input(f"Insira o preço do produto '{produto}': "))
                dict_produtos[lista_keys[1]] = preco
                lista_produtos.append(dict_produtos)
                break
            except ValueError:
                print("Insira apenas números!")

        while True:
            resposta = input("Deseja inserir mais registro? (S/N): ").upper()

            if resposta == "N":
                condicao = False
                break
            elif resposta == "S":
                break
            else:
                print("Insira apenas 'S' ou 'N'!")
    else:
        print("Insira apenas caracteres!")

produto: str = input("Deseja atualizar o preço de qual produto? ")
produto_existe: bool = any(
    item[lista_keys[0]].lower() == produto.lower() for item in lista_produtos
)

if produto_existe:
    for dict_produtos in lista_produtos:
        if dict_produtos[lista_keys[0]].lower() == produto.lower():
            while True:
                try:
                    valor_novo: float = float(
                        input(f"Insira o novo valor do produto '{produto}': ")
                    )
                    valor_antigo: float = dict_produtos["Preço"]
                    dict_produtos["Preço"] = valor_novo
                    print(
                        f"\nO produto '{produto}' teve uma atualização de preço:\nAntigo\tNovo\nR${valor_antigo}\tR${valor_novo}"
                    )
                    break
                except ValueError:
                    print("Insira apenas números!")
            break
else:
    print(f"O produto '{produto}' não existe!")

### 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dict_1: dict = {"Produto": "Porta"}
dict_2: dict = {"Quantidade": 5}

dict_union: dict = {**dict_1, **dict_2}

print(dict_union)

### 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
condicao: bool = True
lista_estoque: list = []
lista_keys: list = ["Produto", "Quantidade"]

while condicao:
    while True:
        dict_produtos: dict = {}
        produto: str = input("Insira o nome do produto: ").strip()

        produto_ja_existe: bool = any(
            item[lista_keys[0]].lower() == produto.lower() for item in lista_estoque
        )

        if produto_ja_existe:
            print("Esse produto já foi adicionado. Por favor, insira outro produto.")
        else:
            break

    if all(caracter.isalpha() or caracter.isspace() for caracter in produto):
        dict_produtos[lista_keys[0]] = produto

        while True:
            try:
                quantidade: int = int(
                    input(f"Insira a quantidade de estoque para {produto}: ")
                )
                dict_produtos[lista_keys[1]] = quantidade
                lista_estoque.append(dict_produtos)
                break
            except ValueError:
                print("Insira apenas números!")

        while True:
            resposta = input("Deseja inserir mais registro? (S/N): ").upper()

            if resposta == "N":
                condicao = False
                break
            elif resposta == "S":
                break
            else:
                print("Insira apenas 'S' ou 'N'!")
    else:
        print("Insira apenas caracteres!")

lista_estoque_filtrado: list = []

for dict_estoque in lista_estoque:
    if dict_estoque[lista_keys[1]] > 0:
        lista_estoque_filtrado.append(dict_estoque)

print("\nOs produtos que possuem unidades no estoque são:")
for dict_estoque in lista_estoque_filtrado:
    print(
        f"- '{dict_estoque[lista_keys[0]]}' possui {dict_estoque[lista_keys[1]]} unidades."
    )

### 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
condicao: bool = True
dict_exemplo: dict = {}
list_keys: list = []
list_values: list = []

while condicao:
    while True:
        key: str = input("Insira a chave do dicionário: ")

        if key in dict_exemplo:
            print(f"A chave '{key}' já existe. Insira outra chave!")
        else:
            value: str = input(f"Insira o valor da chave '{key}': ")
            dict_exemplo[key] = value
            break

    while True:
        resposta: str = input("Deseja inserir outro par chave-valor? (S/N): ").upper()

        if resposta == "N":
            condicao = False
            break
        elif resposta == "S":
            break
        else:
            print("Insira apenas 'S' ou 'N'!")

for key, value in dict_exemplo.items():
    list_keys.append(key)
    list_values.append(value)

print(f"As chaves do dicionário fornecido são: {list_keys}")
print(f"Os valores do dicionário fornecido são: {list_values}")

### 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
while True:
    string: str = input("Digite uma string qualquer: ").lower().strip()

    if all(caracter.isalpha() or caracter.isspace() for caracter in string):
        string_sem_espacos: str = string.replace(" ", "")
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

## Exercícios de Funções


### 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def somar_numeros_lista(lista_numeros: list) -> float:
    """
    Função que recebe uma lista. Verifica se essa lista possui apenas números.
    Retorna a soma dos números da lista.
    """
    soma_lista: float = 0

    for numero in lista_numeros:
        if isinstance(numero, (float, int)) and not isinstance(numero, bool):
            soma_lista += numero

    return soma_lista


if __name__ == "__main__":
    lista = [1, 2, 3, "Bruno", True]
    print(somar_numeros_lista(lista))


### 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def verifica_numero_primo(numero: int) -> bool:
    """
    Função que verifica se um número é primo.

    :param numero: O número a ser verificado.
    :return: True se o número for primo, False caso contrário.
    """
    if isinstance(numero, int) and not isinstance(numero, bool):
        if numero < 2:
            return print(False)

        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return print(False)

        return print(True)

    else:
        return print("A entrada fornecida não é um número inteiro!")


if __name__ == "__main__":
    verifica_numero_primo(5)


### 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverter_string(string: str) -> str:
    """
    Função que verifica se a entrada é uma string. Retira espaços antes/depois da string fornecida. Verifica se a string fornecida está vazia.
    Caso não esteja vazia, verifica se a string fornecida possui apenas caracteres alfanuméricos ou espaços entre as strings.
    Retorna a string revertida.

    :param string: String a ser revertida
    :return: String inserida, porém reveritda
    """
    if isinstance(string, str):
        string_sem_espacos: str = string.strip()

        if string_sem_espacos != "":
            if all(
                caracter.isalpha() or caracter.isspace()
                for caracter in string_sem_espacos
            ):
                string_sem_espacos_revertida: str = string_sem_espacos[::-1]

                return print(string_sem_espacos_revertida)
            else:
                return print(
                    "Forneça apenas caracteres. Não utilize caracteres especiais ou pontuações!"
                )
        else:
            return print("Insira alguma string!")
    else:
        return print("Forneça apenas caracteres!")


if __name__ == "__main__":
    reverter_string("Bootcamp de Python da Jornada de Dados")


### 19. Implemente uma função que receba dois argumentos: uma lista de números e um número.
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def somar_numeros_lista(lista_numeros: list, numero: float) -> list:
    """
    Soma um número a cada elemento de uma lista de números.

    Esta função recebe uma lista de números e um número.
    Retorna uma nova lista onde o número fornecido é somado a cada
    elemento da lista original.

    Args:
        lista_numeros (list): Lista contendo números (int ou float).
        numero (float): Número que será somado a cada elemento da lista.

    Returns:
        list: Nova lista contendo os resultados da soma.

    Raises:
        TypeError: Se lista_numeros não for uma lista ou se numero não for
                   um número válido (int ou float).
        ValueError: Se houver elementos inválidos na lista (que não sejam
                    números int ou float).
    """
    if not isinstance(lista_numeros, list):
        raise TypeError("O primeiro argumento deve ser uma lista.")
    if not isinstance(numero, (int, float)) or isinstance(numero, bool):
        raise TypeError("O segundo argumento deve ser um número válido (int ou float).")

    for num in lista_numeros:
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            raise ValueError(
                "Todos os elementos da lista devem ser números válidos (int ou float)."
            )

    return [num + numero for num in lista_numeros]


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    numero = 2
    print(somar_numeros_lista(lista, numero))


### 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def ordenar_lista_chaves(dados: dict) -> list:
    """
    Função que recebe um dicionário. Verifica se o parâmetro fornecido é um dicionário.
    Se o parâmetro for um dicionário retorna uma lista ordenada de suas chaves.

    :param dados: Dicionário a ser inserido.
    :return: Lista ordenada das chaves do dicionário fornecido.
    """
    if isinstance(dados, dict):
        lista_chaves: list = list(dados.keys())
        lista_chaves.sort()

        return print(lista_chaves)
    else:
        return print("Insira um dicionário!")


if __name__ == "__main__":
    dados_aleatorios = {
        "nome": "João Pereira",
        "idade": 34,
        "cidade": "Rio de Janeiro",
        "salario": 4200.50,
        "empregado": False,
        "empresa": "Tech Solutions",
        "cargo": "Analista de Dados",
        "telefone": "+55 21 98765-4321",
        "email": "joao.pereira@email.com",
        "pontos_fidelidade": 150,
        "ultima_compra": "2024-08-20",
        "assinatura_premium": True,
        "cpf": "123.456.789-00",
        "estado_civil": "Solteiro",
        "altura_metros": 1.75,
    }

    ordenar_lista_chaves(dados_aleatorios)
