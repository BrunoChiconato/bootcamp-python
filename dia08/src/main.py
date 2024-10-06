if __name__ == '__main__':
    pasta = './data/raw'
    caminho_saida = './data/processed'

    df = ler_arquivos_json(pasta)
    df_transformado = calcular_venda_total(df)
    extensao = solicitar_extensao()
    salvar_como(df_transformado, extensao, caminho_saida)