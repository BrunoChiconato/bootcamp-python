from dia07.main import calcular_media_valores_de_lista

def test_calcular_media_valores_de_lista():
    lista_numeros = [1,2,3,4,5]
    resultado = calcular_media_valores_de_lista(lista_numeros)

    assert resultado == 3.0
