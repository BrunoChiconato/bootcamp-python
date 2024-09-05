### 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
### calcule o preço total da lista de compras.

list_produtos = ["maçã", "banana", "cereja"]
dict_produtos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

valor = 0

for key in list_produtos:
    valor += dict_produtos.get(key)

print(f"O valor total da lita de compras é igual a: R${valor}")
