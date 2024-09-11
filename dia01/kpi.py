# Desafio
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000

nome = input("Insira seu nome: ")
salario_mensal = float(input("Insira o valor do seu salário mensal: "))
bonus = float(input("Insira a porcentagem do bônus recebido: "))
kpi = CONSTANTE_BONUS + salario_mensal * bonus

print(f"Olá, {nome}. O seu valor bônus foi de {kpi}")
