# Lista de Exercícios de Python para Engenharia de Dados

**Introdução:**
A seguir, você encontrará uma série de exercícios focados nos conceitos de **listas** e **dicionários** em Python, essenciais para a engenharia de dados. Os exercícios estão organizados em ordem crescente de dificuldade.

## Exercícios

**1. Criação de Lista Simples**
Crie uma lista chamada `numeros` que contenha os números de 1 a 10. Imprima a lista.

**2. Acesso a Elementos da Lista**
Usando a lista `numeros` do exercício anterior, imprima o primeiro e o último elemento.

**3. Slices em Listas**
Imprima os números do índice 2 ao 5 da lista `numeros`.

**4. Adição e Remoção de Elementos**
Adicione o número 11 ao final da lista `numeros` e remova o número 5. Imprima a lista atualizada.

**5. Iteração sobre Listas**
Itere sobre a lista `numeros` e imprima apenas os números pares.

**6. List Comprehension**
Crie uma nova lista chamada `quadrados` que contenha o quadrado de cada número em `numeros` usando list comprehension.

**7. Criação de Dicionário Simples**
Crie um dicionário chamado `aluno` com as seguintes chaves e valores:
- Nome: "João"
- Idade: 20
- Curso: "Engenharia de Dados"

Imprima o dicionário.

**8. Acesso a Valores do Dicionário**
Acesse e imprima o valor associado à chave `Curso` no dicionário `aluno`.

**9. Adição e Remoção em Dicionários**
Adicione uma nova chave `Universidade` com o valor "Universidade X" ao dicionário `aluno`. Remova a chave `Idade`. Imprima o dicionário atualizado.

**10. Iteração sobre Dicionários**
Itere sobre as chaves e valores do dicionário `aluno` e imprima no formato `"chave: valor"`.

**11. Lista de Dicionários**
Crie uma lista chamada `alunos` que contenha três dicionários, cada um representando um aluno com as chaves `Nome`, `Idade` e `Curso`.

**12. Filtragem de Dados em Listas de Dicionários**
Usando a lista `alunos`, filtre e imprima apenas os alunos que estão matriculados em "Engenharia de Dados".

**13. Cálculo Agregado em Listas**
Crie uma lista chamada `notas` contendo as notas [7.5, 8.0, 9.0, 6.5, 10.0]. Calcule e imprima a média das notas.

**14. Contagem de Ocorrências**
Dada a lista `cursos = ["Engenharia", "Dados", "Computação", "Engenharia", "Dados"]`, conte a frequência de cada curso usando um dicionário.

**15. Dicionário Aninhado**
Crie um dicionário chamado `empresa` que contém dois departamentos, cada um com uma lista de funcionários:
```python
empresa = {
    "TI": ["Ana", "Carlos"],
    "RH": ["Bruno", "Daniela"]
}
```
Imprima os nomes dos funcionários do departamento de TI.

**16. Atualização de Valores em Dicionários**
Imagine que a empresa contratou um novo funcionário "Eduardo" para o departamento de TI. Atualize o dicionário `empresa` para incluir esse novo funcionário.

**17. Combinação de Listas em um Dicionário**
Dadas as listas:
```python
chaves = ["a", "b", "c"]
valores = [1, 2, 3]
```
Crie um dicionário que mapeia cada chave ao seu respectivo valor.

**18. Ordenação de Listas**
Ordene a lista `numeros` em ordem decrescente.

**19. Remoção de Duplicatas**
Dada a lista `valores = [1, 2, 2, 3, 4, 4, 5]`, remova os valores duplicados e imprima a lista resultante.

**20. Conversão de Dicionário em Lista**
Converta o dicionário `aluno` em uma lista de tuplas e imprima o resultado.

**21. Agrupamento de Dados**
Dada a lista de dicionários:
```python
vendas = [
    {"produto": "A", "quantidade": 10},
    {"produto": "B", "quantidade": 5},
    {"produto": "A", "quantidade": 7}
]
```
Agrupe as quantidades vendidas por produto em um dicionário.

**22. Leitura de Arquivo Simples**
Leia um arquivo chamado `dados.txt` que contém uma lista de números, um por linha. Armazene os números em uma lista chamada `numeros` e calcule a soma.

**23. Manipulação de Strings em Listas**
Dada a lista `nomes = ["Ana", "Bruno", "Carlos"]`, converta todos os nomes para letras minúsculas.

**24. Funções com Listas e Dicionários**
Escreva uma função `atualizar_estoque(estoque, vendas)` que recebe um dicionário `estoque` e uma lista de dicionários `vendas` e atualiza o estoque subtraindo as quantidades vendidas.

**25. Análise de Dados Simples**
Dada a lista de dicionários representando logs de acesso:
```python
logs = [
    {"usuario": "Ana", "acao": "login"},
    {"usuario": "Bruno", "acao": "logout"},
    {"usuario": "Ana", "acao": "upload"},
    {"usuario": "Carlos", "acao": "login"}
]
```
Conte quantas ações cada usuário realizou e imprima um dicionário com os resultados.

