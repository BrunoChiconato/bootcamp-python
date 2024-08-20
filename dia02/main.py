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
multiplicacao = v1*v2
print(f"A multiplicação de {v1} por {v2} é igual a: {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
v1 = int(input("Insira o primeiro valor: "))
v2 = int(input("Insira o segundo valor: "))
div_inteira = v1//v2
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
media = (v1 + v2)/2
print(f"A média de {v1} e {v2} é igual a: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
v1 = float(input("Insira uma base: "))
v2 = float(input("Insira um expoente: "))
exp = v1**v2
print(f"{v1} elevado a {v2} é igual a: {exp}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
v1 = float(input("Insira a temperatura em graus Celsius: "))
conver_celsius_fahr = (v1 * (9/5)) + 32
print(f"{v1}ºC é igual a: {conver_celsius_fahr}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
r = float(input("Insira o raio do círculo: "))
area_circulo = 3.1415 * r**2
print(f"A área do círculo de raio {r} é igual a: {area_circulo}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação