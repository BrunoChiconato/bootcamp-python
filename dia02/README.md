# Aula 02 - Bootcamp de Python

O repositório oficial desta aula pode ser acessado [aqui](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula02).

## Conceitos Abordados

Nesta aula, exploramos os principais tipos de dados primitivos em Python, incluindo:

- **Inteiros (`int`)**: Representam números inteiros e permitem operações aritméticas como adição, subtração, multiplicação, divisão inteira e módulo.
- **Números de Ponto Flutuante (`float`)**: Representam números reais e suportam operações como adição, subtração, multiplicação, divisão e potenciação.
- **Strings (`str`)**: Sequências de caracteres que permitem operações como conversão para maiúsculas, minúsculas, remoção de espaços e concatenação.
- **Booleanos (`bool`)**: Representam valores lógicos (`True` ou `False`) e suportam operações como `and`, `or`, `not`, igualdade e diferença.

Também discutimos conceitos fundamentais de manipulação de tipos, como:

- **TypeError**: Exceções levantadas quando uma operação ou função é aplicada a um tipo inadequado.
- **Verificação de Tipo (`type check`)**: Uso de `type()` e `isinstance()` para garantir que operações sejam aplicadas a tipos compatíveis.
- **Conversão de Tipo (`type conversion`)**: Uso de funções como `int()`, `float()`, e `str()` para converter valores de um tipo para outro.

## Exercícios

Desenvolvemos uma série de exercícios práticos para reforçar os conceitos discutidos, organizados por tipo de dado. O código desses exercícios pode ser encontrado no arquivo [`main.py`](./main.py).

Também foi proposto um desafio adicional, focado na refatoração do desafio da aula 01 para evitar possíveis bugs. A solução desse desafio está disponível no arquivo [`desafio.py`](./desafio.py).


## Como Executar

Para executar os scripts Python com as soluções dos exercícios, siga os passos abaixo:

1. Certifique-se de que o [Python](https://www.python.org/) esteja instalado em seu sistema.
2. Clone este repositório em seu computador:
   ```sh
   git clone git@github.com:BrunoChiconato/bootcamp-python.git
   ```
3. Navegue até o diretório onde você clonou o repositório. Por exemplo, se você clonou na pasta `Desktop`, use o seguinte comando:
   ```sh
   cd Desktop/bootcamp-python/dia02
   ```
   Se você clonou em outra pasta, ajuste o comando `cd` de acordo:
   ```sh
   cd /caminho/para/o/diretorio/bootcamp-python/dia02
   ```
4. Execute os scripts Python desejados com os seguintes comandos:
   ```sh
   python main.py
   ```
   ```sh
   python desafio.py
   ```

A execução desses scripts permitirá revisar os conceitos abordados e verificar os resultados dos exercícios propostos, bem como explorar os exemplos práticos apresentados na aula.