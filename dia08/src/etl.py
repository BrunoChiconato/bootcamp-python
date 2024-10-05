import pandas as pd #type: ignore
import glob
import os

def ler_arquivos_json(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    df_arquivos_json = [pd.read_json(arquivo_json) for arquivo_json in arquivos_json]
    df_arquivos_json_concatenados = pd.concat(df_arquivos_json, ignore_index=True)

    return df_arquivos_json_concatenados

if __name__ == '__main__':
    pasta = './data/raw'
    print(ler_arquivos_json(pasta))