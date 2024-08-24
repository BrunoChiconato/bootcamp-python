### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
# 1) Solicita ao usuário que digite seu nome
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")

# Verifica se a string contém apenas letras e espaços
if all(char.isalpha() or char.isspace() for char in nome):
    try:
        salario = float(input("Informe seu salário: "))
        try:
            bonus = float(input("Informe o bônus recebido: "))
            valor_final = CONSTANTE_BONUS + salario * bonus
            print(f"Parabéns {nome}! O valor a ser recebido é de: R${valor_final}")
        except ValueError:
            print("O campo bônus só pode conter números")
    except ValueError:
        print("O campo salário só pode conter números")
else:
    print("O campo 'nome' não pode conter caracteres especiais, pontuações e/ou números")
