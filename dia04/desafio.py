# Refatorar o desafio anterior usando Dicionário, Type Hint e Funcões.
def solicita_nome(mensagem: str) -> str:
    """
    Solicita e valida o nome do usuário. O usuário é mantido na função até
    inserir um nome válido.

    Retorna:
        str: Nome válido do usuário.
    """
    while True:
        try:
            nome = input(mensagem).strip()

            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            elif not nome.isalnum():
                raise ValueError("O nome não pode ter caracteres especiais.")
            
            return nome

        except ValueError as e:
            print(f"Erro: {e} Tente novamente.")


def solicita_valor_positivo(mensagem: str) -> float:
    """
    Solicita e valida a entrada de um valor numérico positivo.

    Args:
        mensagem (str): A mensagem a ser exibida ao usuário.

    Retorna:
        float: Valor numérico positivo informado pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                raise ValueError("Por favor, digite um valor positivo.")

            return valor
        
        except ValueError as e:
            print(f"Erro: {e} Tente novamente.")

def calcula_kpi(salario: float, bonus: float) -> float:
    """
    Calcula o KPI baseado no salário e bônus.

    Args:
        salario (float): O salário do usuário.
        bonus (float): O bônus do usuário.

    Retorna:
        float: O valor do KPI calculado.
    """
    bonus_recebido = 1000 + salario * bonus
    return bonus_recebido

if __name__ == "__main__":
    nome = solicita_nome("Digite seu nome: ")
    salario = solicita_valor_positivo("Digite o valor do seu salário: ")
    bonus = solicita_valor_positivo("Digite o valor do bônus recebido: ")
    bonus_recebido = calcula_kpi(salario, bonus)

    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

