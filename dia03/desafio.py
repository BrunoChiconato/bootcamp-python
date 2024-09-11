# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

# Solicita ao usuário que digite seu nome

# Solicita ao usuário que digite o valor do seu salário e converte para float

# Solicita ao usuário que digite o valor do bônus recebido e converte para float

# Imprime as informações para o usuário

CONSTANTE_BONUS = 1000

condicao = True

while condicao:
    nome = input("Digite seu nome: ")

    if all(char.isalpha() or char.isspace() for char in nome):
        while True:
            try:
                salario = float(input("Informe seu salário: "))
                if salario < 0:
                    print("Por favor, digite um valor positivo para o salário.")
                else:
                    break
            except ValueError:
                print("O campo salário só pode conter números")

        while True:
            try:
                bonus = float(input("Informe o bônus recebido: "))
                if bonus < 0:
                    print("Por favor, digite um valor positivo para o salário.")
                else:
                    condicao = False
                    break
            except ValueError:
                print("O campo bônus só pode conter números")
    else:
        print(
            "O campo 'nome' não pode conter caracteres especiais, pontuações e/ou números!"
        )

valor_final = CONSTANTE_BONUS + salario * bonus
print(f"Parabéns {nome}! O valor a ser recebido é de: R${valor_final}")
