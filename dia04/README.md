# Aula 04 - Bootcamp de Python

O repositório oficial desta aula pode ser acessado [aqui](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula04).

## Conceitos Abordados

Nesta aula, exploramos o uso de **Type Hint**, tipos complexos como **Dicionários**, **DataFrames**, **Tabelas**, **Excel**, além de revisarmos **Funções**. Esses tópicos são essenciais para a manipulação e análise eficiente de dados na engenharia de dados.

### Type Hint

O **Type Hint** torna o código mais legível e seguro ao especificar o tipo de dados esperado por variáveis e funções. Isso ajuda a reduzir erros em tempo de execução e facilita a manutenção do código, especialmente quando se trabalha com grandes volumes de dados.

#### Tipagem Fraca vs. Forte

- **Tipagem Forte**: Python exige que tipos sejam compatíveis, não permitindo operações automáticas entre tipos diferentes.
- **Tipagem Fraca**: Linguagens que permitem a conversão automática de tipos diferentes em operações.

#### Tipagem Estática vs. Dinâmica

- **Tipagem Estática**: O tipo das variáveis é definido no momento da compilação.
- **Tipagem Dinâmica**: Python define os tipos das variáveis em tempo de execução, o que permite maior flexibilidade no código.

### Listas e Dicionários

**Listas** e **Dicionários** são fundamentais para a organização de dados:

- **Listas**: Usadas para armazenar coleções ordenadas de dados.
- **Dicionários**: Estruturas que armazenam dados em pares chave-valor, facilitando o acesso e a manipulação de informações.

### Funções

Funções são blocos de código reutilizáveis que permitem modularizar processos repetitivos e lógicos, tornando o código mais organizado e eficiente. Funções em Python também podem ser tipadas com **Type Hint**, o que facilita a leitura e a detecção de erros no código.

## Exercícios

Nesta aula, foram propostos exercícios práticos para reforçar os conceitos de **Type Hint**, **listas**, **dicionários** e **funções**. Esses exercícios exploram diferentes aplicações desses conceitos na resolução de problemas comuns na engenharia de dados.

Também foi proposto um desafio para a refatoração do código da aula anterior, utilizando **Type Hint** e funções para tornar o código mais legível e modular.

O código dos exercícios pode ser encontrado no arquivo [`main.py`](./main.py).

A solução do desafio da aula anterior, com a integração de **Type Hint** e funções, pode ser encontrada no arquivo [`desafio.py`](./desafio.py).

## Como Executar

Para executar os scripts Python com as soluções dos exercícios, siga os passos abaixo:

1. Certifique-se de que o [Python](https://www.python.org/) esteja instalado em seu sistema.
2. Clone este repositório em seu computador:
   ```sh
   git clone git@github.com:seurepositorio/bootcamp-python.git
   ```
3. Navegue até o diretório onde você clonou o repositório:
   ```sh
   cd caminho/para/o/diretorio/bootcamp-python/aula04
   ```
4. Execute os scripts Python desejados com os seguintes comandos:
   ```sh
   python main.py
   ```
   ```sh
   python desafio.py
   ```

A execução desses scripts permitirá revisar os conceitos abordados, verificar os resultados dos exercícios e explorar os exemplos práticos apresentados na aula.