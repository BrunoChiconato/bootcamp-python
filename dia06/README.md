# Novo Projeto de Engenharia de Dados

Este é um guia para inicializar um novo projeto de Engenharia de Dados usando **Poetry** para gerenciamento de dependências e ambientes virtuais, juntamente com **pyenv** para gerenciar as versões do Python.

## Pré-requisitos

Antes de iniciar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- **Python**: Para gerenciar múltiplas versões do Python, recomendamos o uso do [pyenv](https://github.com/pyenv/pyenv). O **pyenv** permite que você controle múltiplas versões do Python no seu sistema, garantindo que você possa trabalhar com diferentes versões em diferentes projetos.
- **Poetry**: O [Poetry](https://python-poetry.org/docs/#installation) é utilizado para gerenciar dependências e criar ambientes virtuais isolados para o projeto.

## Passos para Inicializar um Novo Projeto

### 1. Criar o Projeto com Poetry
Primeiro, crie o projeto usando o Poetry. Isso cria a estrutura básica do projeto e o arquivo `pyproject.toml`.

```bash
poetry new nome_do_projeto
```

Isso criará a seguinte estrutura de diretórios:

``` bash
nome_do_projeto/
│
├── nome_do_projeto/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md
```

O arquivo `__init__.py` marca um diretório como um pacote Python, permitindo que os módulos (arquivos `.py`) dentro desse diretório possam ser importados e usados em outros scripts ou pacotes.

### 2. Navegar para o Diretório do Projeto
Depois de criar o projeto, navegue até o diretório recém-criado:
``` bash
cd nome_do_projeto
```

### 3. Definir a Versão do Python com `pyenv`
O **pyenv** é uma ferramenta para gerenciar múltiplas versões do Python no seu sistema, garantindo que você possa trabalhar com diferentes versões de Python em projetos distintos. Agora, com a pasta do projeto definida, utilize o **pyenv** para instalar e definir a versão do Python que será usada no projeto. Isso criará um arquivo `.python-version` na pasta do projeto:

``` bash
# Instalar a versão desejada do Python (por exemplo, 3.12.5)
pyenv install 3.12.5

# Definir a versão local do Python para o projeto
pyenv local 3.12.5
```

### 4. Configurar o Ambiente Virtual com `Poetry`
Agora, use o **Poetry** para configurar o ambiente virtual. O Poetry criará um ambiente virtual usando a versão do Python definida pelo **pyenv**.

``` bash
# Configura o ambiente virtual para usar o Python 3.12.5
poetry env use 3.12.5
```

### 5. Instalar Dependências
Com o ambiente configurado, você pode instalar as dependências do projeto. Para adicionar pacotes de produção ou desenvolvimento, use os seguintes comandos:

``` bash
# Adicionar uma dependência de produção
poetry add pandas

# Adicionar uma dependência de desenvolvimento
poetry add --dev pytest
```

### 6. Ativar o Ambiente Virtual
Para ativar o ambiente virtual e trabalhar nele, use o comando:

``` bash
poetry shell
```

Se quiser sair do ambiente virtual, use `exit`.

### 7. Gerenciamento de Dependências
Sempre que você precisar instalar todas as dependências de uma vez (por exemplo, ao clonar o projeto em outra máquina), use o comando:
``` bash
poetry install
```

Isso instalará todas as dependências listadas no `pyproject.toml`.

### 8. Executar Scripts ou Comandos no Ambiente Virtual
Para rodar scripts ou comandos dentro do ambiente virtual sem ativá-lo manualmente, você pode usar o comando `poetry run`:

``` bash
# Rodar um script Python
poetry run python nome_do_projeto/main.py

# Rodar os testes
poetry run pytest
```

### 9. Configurar o `.gitignore`
Se você configurar o ambiente virtual dentro da pasta do projeto, certifique-se de adicionar a pasta `.venv/` ao arquivo `.gitignore`, para que o ambiente virtual não seja versionado. Caso você prefira criar o ambiente dentro da pasta do projeto, use o comando:

``` bash
poetry config virtualenvs.in-project true
```

Depois, adicione a pasta `.venv/` ao `.gitignore`:

``` bash
# .gitignore
.venv/
```

## Estrutura Básica do Projeto
Após seguir os passos acima, seu projeto terá a seguinte estrutura básica:

``` bash
nome_do_projeto/
│
├── .venv/  # Ambiente virtual
├── nome_do_projeto/
│   ├── __init__.py
│   └── main.py  # Script principal do projeto
├── tests/
│   ├── __init__.py # Arquivo de teste
│   └── test_funcoes.py
├── pyproject.toml  # Gerenciamento de dependências
└── README.md  # Documentação do projeto

```

- `nome_do_projeto/`: Aqui é onde reside o código principal do seu projeto. O arquivo main.py conterá a função main() e importará outras funções definidas dentro desse pacote ou de outros pacotes.
- `tests/`: Essa pasta conterá os testes do projeto, onde cada arquivo testará as funcionalidades específicas do projeto, garantindo que o código funcione conforme o esperado.

### Fluxo
**1. Executar os testes**:
Em vez de executar o arquivo de teste diretamente (`poetry run tests/test_funcoes.py`), a maneira correta de rodar todos os testes é usando o `pytest`, que é uma ferramenta de teste popular em Python e integrada ao Poetry. O pytest automaticamente descobre e executa qualquer função que comece com `test_` em arquivos que começam com `test_` na pasta `tests/`. Para rodar todos os testes do seu projeto (incluindo `test_funcoes.py`), use o comando:

``` bash
poetry run pytest
```

Esse comando vai executar todos os arquivos de teste localizados na pasta `tests/` e fornecer um relatório sobre quais testes passaram e quais falharam.

**2. Executar o código principal (se os testes passarem)**:
Após verificar que todos os testes passaram com sucesso, você pode então executar o código principal (`main.py`). Para rodar o `main.py` com o Poetry, o comando é:

``` bash
poetry run python nome_do_projeto/main.py
```
### Exemplo
No arquivo `main.py`, você vai colocar a lógica principal do seu projeto. Aqui está um exemplo com uma função `processar_dados`:

``` python
def processar_dados(dados):
    """Função que processa os dados e retorna o resultado."""
    return [dado.upper() for dado in dados]

def main():
    """Função principal que executa o código."""
    dados = ["dado1", "dado2", "dado3"]
    resultado = processar_dados(dados)
    print("Dados processados:", resultado)

if __name__ == "__main__":
    main()
```

Aqui você definiu a função `processar_dados` para fazer o processamento de uma lista de strings, e a função `main()` executa essa lógica quando o script é rodado diretamente.

Agora, você cria testes para essas funções em um arquivo dentro da pasta `tests/`. Esses testes garantem que a função `processar_dados` está funcionando corretamente.

``` python
from nome_do_projeto.main import processar_dados

def test_processar_dados():
    """Testa se a função processar_dados processa corretamente os dados."""
    dados = ["python", "poetry", "pyenv"]
    resultado = processar_dados(dados)

    assert resultado == ["PYTHON", "POETRY", "PYENV"]
```

O comando `assert` é usado para garantir que o resultado esperado seja igual ao resultado da função.

Após isso, quando você rodar o comando:

``` bash
poetry run pytest
```

O **pytest** irá:
- Procurar por arquivos que começam com `test_` na pasta `tests/`.
- Encontrar o arquivo `test_funcoes.py`.
- Executar a função `test_processar_dados()`.

Isso executará apenas os testes no arquivo `test_funcoes.py`. Se você quiser rodar um teste específico dentro desse arquivo, pode indicar o nome do teste:

``` bash
poetry run pytest tests/test_funcoes.py::test_processar_dados
```

Isso executará apenas a função `test_processar_dados` dentro do arquivo `test_funcoes.py`.

## Links Úteis
- Para saber mais sobre `pytest`, visite: [pytest documentation](https://docs.pytest.org/en/stable/).
- Para mais detalhes sobre como configurar o `pyenv`, veja: [pyenv GitHub](https://github.com/pyenv/pyenv).
