import pandas as pd #type: ignore
import glob
import os

def ler_arquivos_json(pasta: str) -> pd.DataFrame:
    """
    Lê todos os arquivos JSON em uma pasta específica e os concatena em um único DataFrame.

    :param str pasta: Caminho para a pasta contendo os arquivos JSON.
    :return: DataFrame contendo os dados concatenados de todos os arquivos JSON.
    :rtype: pd.DataFrame
    :raises ValueError: Se nenhum arquivo JSON válido for encontrado.
    """
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    list_df_arquivos_json = []

    for arquivo_json in arquivos_json:
        try:
            df_arquivos_json = pd.read_json(arquivo_json)
            list_df_arquivos_json.append(df_arquivos_json)
        except ValueError as e:
            print(f'Erro ao ler o arquivo JSON: {e}')

    if list_df_arquivos_json:
        df_arquivos_json_concatenados = pd.concat(list_df_arquivos_json, ignore_index=True)
        return df_arquivos_json_concatenados
    else:
        raise ValueError("Nenhum arquivo JSON válido foi encontrado.")

def calcular_venda_total(arquivo_json: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a venda total multiplicando as colunas 'Quantidade' e 'Venda' e adiciona o resultado 
    como uma nova coluna 'Venda_Total' ao DataFrame.

    :param pd.DataFrame arquivo_json: O DataFrame contendo as colunas 'Quantidade' e 'Venda'.
    :return: O DataFrame original com uma nova coluna 'Venda_Total' adicionada.
    :rtype: pd.DataFrame
    :raises KeyError: Se as colunas 'Quantidade' ou 'Venda' não estiverem presentes no DataFrame.
    """
    if 'Quantidade' in arquivo_json.columns and 'Venda' in arquivo_json.columns:
        arquivo_json['Venda_Total'] = arquivo_json['Quantidade'] * arquivo_json['Venda']

        return arquivo_json
    else:
        raise KeyError("As colunas 'Quantidade' e 'Venda' são necessárias para o cálculo.")

def solicitar_extensao():
    """
    Solicita ao usuário o formato de arquivo de saída (CSV ou Parquet) até que uma resposta válida seja fornecida.

    :return: A extensão escolhida pelo usuário ('csv' ou 'parquet').
    :rtype: str
    """
    while True:
        extensao: str = input('Deseja salvar como? (csv/parquet): ').strip().lower()

        if extensao in ['csv', 'parquet']:
            return extensao
        else:
            print("Insira apenas 'csv' ou 'parquet'!")
    
def salvar_como(arquivo_json: pd.DataFrame, extensao: str, path: str):
    """
    Salva o DataFrame em um arquivo no formato especificado (CSV ou Parquet).

    :param pd.DataFrame arquivo_json: O DataFrame a ser salvo.
    :param str extensao: A extensão de arquivo escolhida pelo usuário ('csv' ou 'parquet').
    :param str path: Caminho para o diretório onde o arquivo será salvo.
    :return: None
    """
    output_file = os.path.join(path, f'vendas.{extensao}')

    if extensao == 'csv':
        arquivo_json.to_csv(output_file, index=False)
    elif extensao == 'parquet':
        arquivo_json.to_parquet(output_file, index=False)

    print(f'Arquivo salvo em: {output_file}')