# Exercícios

# 1. Calcular Média de Valores em uma Lista
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

# 3. Contar Valores Únicos em uma Lista

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

# 6. Encontrar Valores Ausentes em uma Sequência


def main():
    lista_numeros = [0.0]
    print(conversao_celsius_fahrenheit(lista_numeros))

if __name__ == "__main__":
    main()