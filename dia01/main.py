# Exercício 01: Crie um programa que o usuário digita o seu nome e retorna o número de caracteres
print("A quantidade de caracteres do seu nome é:", len(input("Digite seu nome: ")))

# Exercício 02: Crie um programa onde o usuário digita dois valores e retorne a soma
print("Digite dois valores numéricos:")
v1 = float(input())
v2 = float(input())
print(f"A soma de {v1} e {v2} é igual a:", v1 + v2)

# Exercício 03: Refatore o exercício 01 atribuindo variáveis
nome = input("Digite seu nome: ")
quantidade_letras = len(nome)
print(f"A quantidade de caracteres no seu nome é:: {quantidade_letras}")



