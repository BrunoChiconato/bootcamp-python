### 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
list_numeros = list(range(1,11))

for num in list_numeros:
    num_quadrado = num ** 2
    print(f"- {num} ao quadrado = {num_quadrado}")
