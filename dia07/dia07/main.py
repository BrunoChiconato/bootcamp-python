# Exercícios

# 1. Calcular Média de Valores em uma Lista
from typing import List


def calcular_media_valores_de_lista(lista_num: list) -> float:
    media: float = 0
    soma: float = 0
    contador: int = 0

    try:
        if not isinstance(lista_num, list):
            raise TypeError("O parâmetro fornecido não é uma lista!")
    
        for num in lista_num:
            try:
                if isinstance(num, (int, float)) and not isinstance(num, bool):
                    soma += num
                    contador += 1
                else:
                    raise TypeError(f"O elemento '{num}' não é um número!")
                
            except Exception as e:
                print(f"Erro: {e} Tente novamente.")
                return 0.0
        
        if contador == 0:
            raise ValueError("A lista não possui nenhum elemento válido!")
        
        media = soma / contador
                
    except Exception as e:
        print(f"Erro: {e} Tente novamente.")
        return 0.0 

    return media       

# 2. Filtrar Dados Acima de um Limite
def filtrar_dados_acima_de_limite(lista_nums: list, limite: int) -> list:
    lista_nums_filtrada: list = []

    try:
        if not isinstance(lista_nums, list):
            raise TypeError("O parametro fornecido não é uma lista!")
        
        if not isinstance(limite, (int,float)) or isinstance(limite, bool):
            raise TypeError("O parametro fornecido não é um inteiro/float!")
        
        for nums in lista_nums:
            try:
                if not isinstance(nums, (int,float)) or isinstance(nums, bool):
                    raise TypeError(f"O elemento '{nums}' não é um inteiro/float!")
                
                if nums > limite:
                    lista_nums_filtrada.append(nums)
                
            except Exception as e:
                print(f"Erro: {e} Tente novamente.")
                return []

        if len(lista_nums_filtrada) == 0:
            raise ValueError("Nenhum elemento foi inserido na lista/Todos os elementos estão abaixo do limite!")
    except Exception as e:
        print(f"Erro: {e} Tente novamente.")
        return []
    
    return lista_nums_filtrada

# 3. Contar Valores Únicos em uma Lista
def contar_valores_unicos(lista_valores: list) -> list:
    dict_aux: dict = {}
    lista_aux: list = []

    try:
        if not isinstance(lista_valores, list):
            raise TypeError("O parametro fornecido não é uma lista!")
        
        if len(lista_valores) == 0:
            raise TypeError("A lista está vazia!")
        
        for valor in lista_valores:
            if isinstance(valor, str):
                valor = valor.lower()
            
            if valor in dict_aux:
                dict_aux[valor] += 1
            elif valor not in dict_aux:
                dict_aux[valor] = 1

        for key, value in dict_aux.items():
            if value == 1:
                lista_aux.append(key)

    except Exception as e:
        print(f"Erro: {e} Tente novamente.")
        return []
    
    return len(lista_aux)

# 4. Converter Celsius para Fahrenheit em uma Lista
def conversao_celsius_fahrenheit(temps_celsius: list) -> list:
    temps_fahrenheit: list = []
    contador: int = 0

    try:
        if not isinstance(temps_celsius, list):
            raise TypeError("O parametro fornecido não é uma lista!")
        
        for temp_celsius in temps_celsius:
            try:
                if not isinstance(temp_celsius, float) and isinstance(temp_celsius, bool):
                    raise TypeError(f"O elemento '{temp_celsius}' não é uma temperatura válida!")
                
                temp_fahrenheit: float = temp_celsius * (9/5) + 32
                temps_fahrenheit.append(temp_fahrenheit)
                contador += 1
                
            except Exception as e:
                    print(f"Erro: {e} Tente novamente.")
                    return []
        
        if contador == 0:
            raise ValueError("A lista não possui nenhum elemento válido!") 

    except Exception as e:
        print(f"Erro: {e} Tente novamente.")
        return []
    
    return temps_fahrenheit

# 5. Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(lista_nums: list) -> float:
    import numpy as np # type: ignore

    valores_validos = []

    try:
        if not isinstance(lista_nums, list):
            raise TypeError("O parametro fornecido não é uma lista!")
        
        for num in lista_nums:
            try:
                if not isinstance(num, (int,float)) or isinstance(num, bool):
                    raise TypeError(f"O elemento '{num}' não é um inteiro/float!")
                
                valores_validos.append(num)
                
            except Exception as e:
                print(f"Erro: {e} Tente novamente.")
                return 0.0

        if len(valores_validos) == 0:
            raise ValueError("A lista não possui nenhum elemento válido!") 
        
        desvio_padrao = np.std(valores_validos)

    except Exception as e:
        print(f"Erro: {e} Tente novamente.")
        return 0.0

    return desvio_padrao

# 6. Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    from typing import List

    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))  

def main():
    lista_valores = ["brasil", "Brasil", "BRASIL", 2, 4, 1]
    print(contar_valores_unicos(lista_valores))

if __name__ == "__main__":
    main()