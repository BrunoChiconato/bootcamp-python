import pandas as pd #type: ignore
import glob
import os

def ler_arquivos_json(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    df_arquivos_json = [pd.read_json(arquivo_json) for arquivo_json in arquivos_json]
    df_arquivos_json_concatenados = pd.concat(df_arquivos_json, ignore_index=True)

    return df_arquivos_json_concatenados

def calcular_venda_total(arquivo_json: pd.DataFrame) -> pd.DataFrame:
    if 'Quantidade' in arquivo_json.columns and 'Venda' in arquivo_json.columns:
        arquivo_json['Venda_Total'] = arquivo_json['Quantidade'] * arquivo_json['Venda']
        
        return arquivo_json
    else:
        raise KeyError("As colunas 'Quantidade' e 'Venda' são necessárias para o cálculo.")

def solicitar_extensao():
    while True:
        extensao: str = input('Deseja salvar como? (csv/parquet): ').strip().lower()

        if extensao in ['csv', 'parquet']:
            return extensao
        else:
            print("Insira apenas 'csv' ou 'parquet'!")
    
def salvar_como(arquivo_json: pd.DataFrame, extensao: str, path: str):
    output_file = os.path.join(path, f'vendas.{extensao}')

    if extensao == 'csv':
        arquivo_json.to_csv(output_file, index=False)
    elif extensao == 'parquet':
        arquivo_json.to_parquet(output_file, index=False)

    print(f'Arquivo salvo em: {output_file}')

if __name__ == '__main__':
    pasta = './data/raw'
    caminho_saida = './data/processed'

    df = ler_arquivos_json(pasta)
    df_transformado = calcular_venda_total(df)
    extensao = solicitar_extensao()
    salvar_como(df_transformado, extensao, caminho_saida)
