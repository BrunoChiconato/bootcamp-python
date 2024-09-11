## Strings

# 2.3 – Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e
# apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples,
# como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.
nome = "Bruno"
print(f"Alô {nome}, você gostaria de aprender um pouco de Python hoje?")

# 2.4 – Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma
# pessoa em uma variável e então apresente o nome dessa pessoa em letras
# minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula.
nome = "Bruno"
nome_maiusculo = nome.upper()
nome_minisculo = nome.lower()
nome_capitalizado = nome.title()
print(
    f"Nome em maiúsculo: {nome_maiusculo}\nNome em minúsculo: {nome_minisculo}\nNome capitalizado: {nome_capitalizado}"
)

# 2.5 – Citação famosa: Encontre uma citação de uma pessoa famosa que você
# admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência
# a seguir, incluindo as aspas: Albert Einstein certa vez disse: “Uma pessoa que
# nunca cometeu um erro jamais tentou nada novo.”
citacao = '"Uma pessoa que nunca cometeu um erro jamais tentou nada novo."'
print(f"{citacao}")

# 2.6 – Citação famosa 2: Repita o Exercício 2.5, porém, desta vez, armazene o
# nome da pessoa famosa em uma variável chamada famous_person. Em
# seguida, componha sua mensagem e armazene-a em uma nova variável
# chamada message. Exiba sua mensagem.
famous_person = "Albert Einstein"
message = '"Uma pessoa que nunca cometeu um erro jamais tentou nada novo."'
print(f"{message} - {famous_person}")

# 2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
# pessoa e inclua alguns caracteres em branco no início e no final do nome.
# Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
# uma vez.
nome_1 = " Bruno "
nome_2 = "    Emanuelle"
nome_3 = "Jorge  "
nome_1_sem_espaco = nome_1.strip()
nome_2_sem_espaco = nome_2.strip()
nome_3_sem_espaco = nome_3.strip()
print(
    f"Nomes sem espaço em branco no início ou fim:\n\t-{nome_1_sem_espaco}\n\t-{nome_2_sem_espaco}\n\t-{nome_3_sem_espaco}"
)
