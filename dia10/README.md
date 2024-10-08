# Aula 10: Exercícios de Decoradores para Engenharia de Dados

O repositório oficial desta aula pode ser acessado [aqui](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados).

## Conteúdo

Esta aula foi apenas uma revisão. Como decoradores foi o último conteúdo abordado essa pasta contém exercícios voltados ao aprendizado de **decoradores** no contexto da **Engenharia de Dados**.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **Exercício 1**: Logging de tempo de execução com decoradores.
- **Exercício 2**: Validação de entrada de dados com decoradores.
- **Exercício 3**: Implementação de cache para evitar recomputação de resultados.
- **Exercício 4**: Limite de chamadas a uma função decorada.
- **Exercício 5**: Implementação de "retry" em caso de falha, para reexecutar uma função.

## Exercícios

### Exercício 1: Logging de Tempo de Execução

Crie um decorador chamado `log_execution_time` que mede e registra o tempo de execução de uma função. Ele deve imprimir o tempo total ao final da execução.

Exemplo de função a ser decorada:

```python
import time

def process_data():
    time.sleep(2)
    print("Dados processados")
```

Você deve aplicar o decorador à função `process_data` para monitorar o tempo gasto na execução.

---

### Exercício 2: Validação de Entrada de Dados

Crie um decorador chamado `validate_data` que verifica se os dados passados para uma função são uma lista de dicionários, e se cada dicionário contém as chaves `id`, `nome` e `idade`. Se os dados forem inválidos, deve ser lançada uma exceção `ValueError`.

Exemplo de função a ser decorada:

```python
def insert_data_in_database(data):
    print(f"Inserindo {len(data)} registros no banco de dados")
```

Teste o decorador passando dados válidos e inválidos.

---

### Exercício 3: Cache de Resultados

Implemente um decorador `cache_results` que armazena os resultados de chamadas anteriores de uma função. Se a função for chamada novamente com os mesmos parâmetros, o decorador deve retornar o resultado em cache em vez de recalcular.

Exemplo de função a ser decorada:

```python
def heavy_computation(a, b):
    print(f"Processando dados com {a} e {b}...")
    time.sleep(3)
    return a + b
```

A função `heavy_computation` deve ser decorada para utilizar o cache.

---

### Exercício 4: Controle de Requisições

Crie um decorador chamado `limit_calls` que limita o número de vezes que uma função pode ser chamada. Se a função for chamada mais vezes do que o limite permitido, o decorador deve levantar uma exceção `RuntimeError`.

Exemplo de função a ser decorada:

```python
def get_data_from_api():
    print("Fazendo requisição para a API")
    return {"data": "valor"}
```

Configure o decorador para permitir apenas 5 chamadas à função.

---

### Exercício 5: Retry em Caso de Falha

Crie um decorador chamado `retry_on_failure` que tenta reexecutar uma função até 3 vezes se ela levantar uma exceção. Após 3 tentativas falhas, deve-se desistir e permitir que a exceção seja propagada.

Exemplo de função a ser decorada:

```python
import random

def fetch_data_from_database():
    if random.choice([True, False]):
        raise ConnectionError("Falha na conexão com o banco de dados")
    print("Dados obtidos com sucesso")
```

Aplique o decorador para que a função `fetch_data_from_database` seja tentada novamente em caso de falha.

---

## Como Executar

Para executar o script Python com os exercícios, siga os passos abaixo:

1. Certifique-se de que o [Python](https://www.python.org/) e o [Poetry](https://python-poetry.org/docs/#installation) estejam instalados em seu sistema.
2. Clone este repositório em seu computador:

   ```sh
   git clone git@github.com:seurepositorio/bootcamp-python.git
   ```

3. Navegue até o diretório da aula:

   ```sh
   cd caminho/para/o/diretorio/bootcamp-python/aula08
   ```

4. Instale as dependências do projeto usando o Poetry:

   ```sh
   poetry install
   ```

5. Execute o script Python:

   ```sh
   poetry run python main.py
   ```
