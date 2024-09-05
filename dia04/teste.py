while True:
    string = input("Digite uma string qualquer: ").lower().strip()

    if all(caracter.isalpha() or caracter.isspace() for caracter in string):
        string_sem_espacos = string.replace(" ","")
        dict_caracteres = {}

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
