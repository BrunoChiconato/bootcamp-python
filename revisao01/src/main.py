# 1. Criação de Lista Simples
# Crie uma lista chamada `numeros` que contenha os números de 1 a 10. 
# Imprima a lista.
lista_numeros: list = list(range(1,11))
print(lista_numeros)

# 2. Acesso a Elementos da Lista
# Usando a lista numeros do exercício anterior, imprima o primeiro e o último elemento.
print(f"Primeiro elemento: {lista_numeros[0]}\nÚltimo elemento: {lista_numeros[9]}")

# 3. Slices em Listas
# Imprima os números do índice 2 ao 5 da lista numeros.
print(f"Elementos do índice 2 ao 5: {lista_numeros[2:6]}")

# 4. Adição e Remoção de Elementos 
# Adicione o número 11 ao final da lista numeros e remova o número 5. 
# Imprima a lista atualizada.
lista_numeros.append(11)
print(f"Adicionando o número 11 a lista: {lista_numeros}")
lista_numeros.remove(5)
print(f"Removendo o numero 5 da lista: {lista_numeros}")

# 6. List Comprehension 
# Crie uma nova lista chamada quadrados que contenha o quadrado de cada número
# em numeros usando list comprehension.
quadrados = [num ** 2 for num in lista_numeros]
print(f"Lista que contém o quadrado dos números em 'numeros': {quadrados}")