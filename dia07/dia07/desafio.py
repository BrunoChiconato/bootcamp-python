import csv

def ler_csv(path_csv) -> list:
    with open(path_csv, mode="r", encoding="utf-8") as base:
        leitor = csv.DictReader(base)
        return list(leitor)

def processar_dados(base_csv: list) -> dict:
    categorias: dict = {}

    for dicts in base_csv:
        categoria: str = dicts["Categoria"]

        if categoria not in categorias:
            categorias[categoria] = []
            
        categorias[categoria].append(dicts)

    return categorias
    
def calcular_vendas_categoria(categorias: dict):
    vendas_por_categorias: dict = {}

    for categoria, dados in categorias.items():
        quantidade: float = 0
        venda: float = 0
        valor_total: float = 0

        for dado in dados:
            quantidade = float(dado["Quantidade"])
            venda = float(dado["Venda"])
            valor_total += quantidade * venda

        vendas_por_categorias[categoria] = valor_total

    return vendas_por_categorias

def main():
    path_csv = "../data/base_produtos_100000.csv"

    base_csv = ler_csv(path_csv)
    categorias = processar_dados(base_csv)
    total_vendas = calcular_vendas_categoria(categorias)

    print("O total de vendas por categoria é igual a:")
    for key, value in total_vendas.items():
        formatted_value = f"{value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"- {key} = R$ {formatted_value}")
    
if __name__ == "__main__":
    main()
