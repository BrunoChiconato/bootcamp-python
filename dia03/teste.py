condicao = True
list_dict_transacao = []
keys = ["valor", "hora"]

while condicao:
    dict_transacao = {}

    for key in keys:
        value = input(f"Informe o valor para o campo '{key}': ")

        if value.isdigit():
            dict_transacao[key] = value
        else:
            print("Insira apenas valores numéricos!")
            break

    if len(dict_transacao) == len(keys):
        list_dict_transacao.append(dict_transacao)

    resposta = input("Deseja inserir mais transações? (S/N): ")
    if resposta.upper() == "N":
        condicao = False
    elif resposta.upper() != "S":
        print("Insira apenas 'S' ou 'N'")

for i, trans in enumerate(list_dict_transacao):
    valor = float(trans.get("valor"))
    hora = int(trans.get("hora"))

    if valor > 10000:
        print(f"Sua {i+1}ª transação é suspeita, pois o valor a ser transferido foi de: R$ {valor}")
    elif hora < 9 or hora > 18:
        print(f"Sua {i+1}ª transação é suspeita, pois a hora da transferência foi às: {hora}h")