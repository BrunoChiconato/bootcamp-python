from etl import ler_arquivos_json, calcular_venda_total, solicitar_extensao, salvar_como

def main():
    caminho_raw = './data/raw'
    caminho_processed = './data/processed'

    df_original = ler_arquivos_json(caminho_raw)
    df_transformado = calcular_venda_total(df_original)
    extensao = solicitar_extensao()
    salvar_como(df_transformado, extensao, caminho_processed)

if __name__ == '__main__':
    main()