Notas do curso

# Links úteis

- https://jitsi.4linux.com.br/testeJitsiMeet
- https://moodle-prod.4linux.com.br/login/4linux/login/index.html?errorcode=4
- https://rentry.co/8070
- Certificação de Python: PCAP
- Repositório das aulas: https://bitbucket.org/mi3mi/8070-python-fundamentals/src/main/
- Dica para wiki: https://js.wiki/get-started

# Roadmap do curso

- Introdução
  - Aspectos da linguagem
  - Pensar computacionalmente
  - Tipos de dados ("Primitivos")
    - Numéricos (Inteiros, Floats)
    - Sequencias (Strings)
  - Lógica, Estruturas de Decisão
  - Estruturas de Repetição
  - Coleções
    - Listas, Tuplas, Dicionários <- JSON, YAML <> JSON
- Funções
  - O que é função?
  - Quais são os seus usos?
  - Tipos
    - Nativas (built in)
    - Módulos
    - Definidas pelos usuários
    - Anônimas
- Módulo e pacotes
  - Entender o que é um módulo em python
  - Como instalar módulos de terceiros através do PIP
  - Como criar ambientes virtuais <> requirements.txt
  - Como criar um Módulo/Pacote
  - Estrutura de projeto
- Arquivos
  - Abordagem de uso de arquivo
  - Tipos de arquivo
    - TXT/texto puro
    - CSV – Comma Separated Values
    - JSON
    - YAML <= Arquivos de configuração
- Introdução à Orientação à Objetos com Python
  - O que é esse paradigma de programação
  - Quais as principais features
    - Abstração
    - Encapsulamento
    - Herança
    - Polimorfismo
- Exercícios/Projeto
- Versionamento de código com o Git
  - O que é o Git?
  - Quais os seus principais comandos:
    - Identidade
    - Gerenciamento de Servidor Remoto
    - Branches
    - Reescreve a história do git -> rebase
    - Comandos que requerem cuidado! Git reset
    - Workflows
    - GitFlow
    - Trunk Based Flow <- ci/ cd
- Python para APIs
  - Cliente de python para consumir
  - O que é uma API
  - Protocolo http
  - Principais representações do protocolo HTTP
  - Criar automações a partir disso
- Extras
  - Testes
  - Banco de dados
  - Módulos/CLI

# Introdução

- Guido van Rossum
- Crítica à linguagem C
- Época do https://pt.wikipedia.org/wiki/Andrew_Stuart_Tanenbaum
- Sua simplicidade possibilitou ser aplicada em infra, dados, aplicações, etc.
- O Python delega sua computação para outras linguagens
- Python se popularizou muito pelo Data Science
- Os seus maiores projetos são dedicados para Infra
- Nessa época, o Ruby era muito famoso, mas estava decaindo
  - Ruby on Rails

# Interpretador

- Lê instruções em um formato mais simples (sintaxe de python) -> <jython, cpython, pypy>
- Faz uso de garbage collector
- Para executar um arquivo python, você pode usar o python3 NOME_ARQUIVO.py ou colocar no topo do arquivo #!/usr/bin/python3 ("chmod +x ex01.py")

```bash
>> python3 –i NOME_ARQUIVO.py
```

- Ao final da execução, mantenho a seção no interpretador

# Tipos de dados

- Python não e fortemente tipado
- Dados imutáveis, que não se modificam
  - Um pouco mais agil do que trabalhar com os dados mutáveis

## Inteiro e float

```python
>>> n1 = 10
>>> type(n1)
<class 'int'>
>>> # estou atribuindo um espaço na memoria com o valor 10
>>> # estou atribuindo o valor 10 na variavel "n1"
>>> n1
10
>>> print(n1)
10
>>> print(n1 + 1)
11
>>> n1
10
>>> n1 + 100
110
>>> n1
10
>>> id(n1)
9789280
>>> n1 = n1 + 100
>>> id(n1)
9792480
>>> n1
110
>>> n2 = 10.5
>>> type(n2)
<class 'float'>
>>> n1 + n2
120.5
>>> 10 / 2
5.0
>>> # todo resultado em uma divisao e um numero flutuante
>>> n1 ** n2
2.7203400420274964e+21
>>> 2 ** 4
16
>>> n1 * n2
1155.0
>>> n1 // n2
10.0
>>> n1 % n2
5.0
```

## String

- Sequência de caracteres
- Python permite acessar trechos dessa sequência

```python
>>> texto = '4Linux Open Software Specialists'
>>> texto
'4Linux Open Software Specialists'
>>> # 4Linux Open Software Specialists
>>> # 0123456789...
>>> texto[1]
'L'
>>> # 4Linux Open Software Specialists
>>> #                                -1
>>> texto[-1]
's'
>>> texto[-2]
't'
>>> len(texto)
32
>>> texto[32]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> texto[31]
's'
>>> texto[0:10]
'4Linux Ope'
>>> # Slicing
>>> texto[10]
'n'
>>> # No slicing o 10 esta fora do intervalo
>>> texto[0:-1]
'4Linux Open Software Specialist'
>>> texto[0:-1:2]
'4iu pnSfwr pcait'
>>> # Pulando caracteres
>>> texto[0:-1:1]
'4Linux Open Software Specialist'
>>> texto.capitalize()
'4linux open software specialists'
>>> texto
'4Linux Open Software Specialists'
>>> texto.capitalize()
'4linux open software specialists'
>>> texto
'4Linux Open Software Specialists'
>>> texto.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: count() takes at least 1 argument (0 given)
>>> texto.count('a')
2
>>> texto
'4Linux Open Software Specialists'
>>> texto.count('o')
1
>>> texto.lower().count('o')
2
>>> texto.
texto.capitalize(    texto.endswith(      texto.index(         texto.isdigit(       texto.isspace(       texto.lower(         texto.rfind(         texto.rstrip(        texto.swapcase(
texto.casefold(      texto.expandtabs(    texto.isalnum(       texto.isidentifier(  texto.istitle(       texto.lstrip(        texto.rindex(        texto.split(         texto.title(
texto.center(        texto.find(          texto.isalpha(       texto.islower(       texto.isupper(       texto.maketrans(     texto.rjust(         texto.splitlines(    texto.translate(
texto.count(         texto.format(        texto.isascii(       texto.isnumeric(     texto.join(          texto.partition(     texto.rpartition(    texto.startswith(    texto.upper(
texto.encode(        texto.format_map(    texto.isdecimal(     texto.isprintable(   texto.ljust(         texto.replace(       texto.rsplit(        texto.strip(         texto.zfill(
>>> texto.split()
['4Linux', 'Open', 'Software', 'Specialists']
>>> texto.startswith('4')
True
>>> texto.startswith('23123213213')
False
>>> texto.endswith('23123213213')
False
>>> texto2 = ' 4Linux Open Software Specialists '
>>> texto2.strip()
'4Linux Open Software Specialists'
>>> texto2.rstrip()
' 4Linux Open Software Specialists'
>>> texto2.lstrip()
'4Linux Open Software Specialists '
>>> texto2.replace(' ', 'x')
'x4LinuxxOpenxSoftwarexSpecialistsx
```

- https://docs.python.org/3/library/string.html#formatstrings

## Listas, Tuplas e Dicionários

- Carregam mais de um tipo de informação

### Tupla

- Tipo de dados imutável
- O Python sempre tentará trabalhar com tuplas por debaixo dos panos

```python
>>> tupla.
tupla.count(  tupla.index(
>>> tupla.count(2)
1
>>> tupla.index("jujuba")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
>>> tupla.index("textp")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
>>> tupla.index("texto")
5
>>> tupla[5]
'texto'
>>> id(tupla)
140343017811072
>>> tupla
(1, 2, 3, 4, 5, 'texto', 10.5, (0, 1, 2, 3))
>>> tupla = ("jujuba", "qualquer coisa")
>>> id(tupla)
140342995672320
```

### Lista

- Lista é alterada por referência

```python
>>> lista
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5, (0, 1, 2, 3, 4)]
>>> id(lista)
140374350278080
>>> lista[-1] = [0,2,4,6,8]
>>> lista
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5, [0, 2, 4, 6, 8]]
>>> id(lista)
140374350278080
>>> lista.
lista.append(   lista.clear(    lista.copy(     lista.count(    lista.extend(   lista.index(    lista.insert(   lista.pop(      lista.remove(   lista.reverse(  lista.sort(
>>> lista.append("qualquer coisa")
>>> lista
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5, [0, 2, 4, 6, 8], 'qualquer coisa']
>>> lista.pop()
'qualquer coisa'
>>> lista
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5, [0, 2, 4, 6, 8]]
>>> lista.insert(0, "outro elemento")
>>> lista
['outro elemento', 0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5, [0, 2, 4, 6, 8]]
>>> lista.remove("jujuba")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> lista.clear()
>>> lista
[]
>>> lista = [0, 1, 2, 3, 4, [0,1,2,3,4], "texto", 10.5, (0,1,2,3,4)]
>>> copia = lista.copy()
>>> copia
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5, (0, 1, 2, 3, 4)]
>>> id(lista)
140374350278208
>>> id(copia)
140374330525312
>>> varx = copia
>>> id(varx)
140374330525312
>>> id(varx) == id(copia)
True
>>> copia.pop()
(0, 1, 2, 3, 4)
>>> copia
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5]
>>> varx
[0, 1, 2, 3, 4, [0, 1, 2, 3, 4], 'texto', 10.5]
>>> lista[0]
0
>>> lista[-1]
(0, 1, 2, 3, 4)
>>> len(lista)
9
```

### Dicionários

```python
>>> pessoa[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> pessoa['nome']
'Guido van Rossum'
>>> pessoa
{'nome': 'Guido van Rossum', 'nacionalidade': 'Holandesa', 'idade': 56}
>>> pessoa.
pessoa.clear(       pessoa.copy(        pessoa.fromkeys(    pessoa.get(         pessoa.items(       pessoa.keys(        pessoa.pop(         pessoa.popitem(     pessoa.setdefault(  pessoa.update(      pessoa.values(
>>> pessoa.keys()
dict_keys(['nome', 'nacionalidade', 'idade'])
>>> pessoa.values()
dict_values(['Guido van Rossum', 'Holandesa', 56])
>>> pessoa.get('nome')
'Guido van Rossum'
>>> pessoa.get('nao-existe')
>>> pessoa['nao-existe']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'nao-existe'
>>> pessoa.pop('nome')
'Guido van Rossum'
>>> pessoa
{'nacionalidade': 'Holandesa', 'idade': 56}
>>> del pessoa['nacionalidade']
>>> pessoa
{'idade': 56}
>>> pessoa['linguagem'] = 'Python'
>>> pessoa
{'idade': 56, 'linguagem': 'Python'}
>>> pessoa.items()
dict_items([('idade', 56), ('linguagem', 'Python')])
```

## Pensar computacionalmente

- Problema -> Problema de computação -> linguagem (python)
- Exercício: receba dois números e apresente a sua soma

```python
Informe o primeiro número:10
Informe o segundo número:10
1010
>>> type(n1)
<class 'str'>
>>> print('isso e um texto com apostrofe\'s')
isso e um texto com apostrofe's
>>> print("isso e um texto com apostrofe\"s")
isso e um texto com apostrofe"s
>>> 'texto1' + 'texto2'
'texto1texto2'
>>> # concatenaçao
>>> soma
'1010'
>>> type(input("n1: "))
n1: 10
<class 'str'>
>>> 'texto1' * 2
'texto1texto1'
>>> 'texto1' / 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 'texto1' - 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

- O Python usa a notação americana de . e não ,

## Repetição

### Listas e Tuplas

```python
>>> for numero in range(0, 11):
...   print(numero)
...
0
1
2
3
4
5
6
7
8
9
10
>>> lista = ["texto", "outro item", 4.5]
>>> for indice in range(0, len(lista)):
...   print(lista[indice])
...
texto
outro item
4.5
>>> enumerate(lista)
<enumerate object at 0x7fad9c31c280>
>>> for i in enumerate(lista):
...   print(i)
...
(0, 'texto')
(1, 'outro item')
(2, 4.5)
```

### Dicionários

```python
>>> dic = { 'nome': 'Guido Van Rossum', 'nacionalidade': 'Holandesa' }
>>> for item in dic:
...   print(item)
...
nome
Nacionalidade
>>> for valor in dic.values():
...   print(valor)
...
Guido Van Rossum
Holandesa
>>> for chave, valor in dic.items():
...   print(f"Chave: {chave}, Valor: {valor}")
...
Chave: nome, Valor: Guido Van Rossum
Chave: nacionalidade, Valor: Holandesa
```

## Dicionário

```python
>>> dic
{'nome': 'Guido Van Rossum', 'idade': 45, 'linguagem': ['Python', 'C'], 'nacionalidade': 'Holandesa', 'empresas': {'microsoft': {'data-inicio': '17/09/2017', 'data-fim': ''}, 'ABC': {'data-inicio': '10/04/1991', 'data-fim': '10/08/1999'}}}
>>> dic['linguagem']
['Python', 'C']
>>> dic['linguagem'][1]
'C'
>>> dic['empresas']
{'microsoft': {'data-inicio': '17/09/2017', 'data-fim': ''}, 'ABC': {'data-inicio': '10/04/1991', 'data-fim': '10/08/1999'}}
>>> dic['empresas']['ABC']['data-fim']
'10/08/1999'
>>> user
{'username': 'gvrossum_3@4linux.com.br', 'password': 'lakdj21', 'expired': True}
>>> user.get('asasas')
>>> teste = user.get('asasas')
>>> teste
>>> type(teste)
<class 'NoneType'>
>>> teste is None
True
>>> teste is not None
False
```

## Comparação

```python
>>> 10 > 5
True
>>> True
True
>>> False
False
>>> type(True)
<class 'bool'>
>>> 10 < 14
True
>>> 10 > 14
False
>>> 10 <= 14
True
>>> 10 >= 14
False
>>> 10 != 14
True
>>> 10 == 14
False
>>> maior_valor = 0
>>> maior_valor > v1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'v1' is not defined
>>> v1 = 10
>>> maior_valor > v1
False
>>> if maior_valor < v1:
...   print(v1)
...
10
>>> v1 = 9
>>> if maior_valor < v1:
...   print(v1)
...
9
>>> maior_valor = 100
>>> if maior_valor < v1:
...   print(v1)
...
>>> maior_valor < v1
False
>>> user
{'username': 'gvrossum_3@4linux.com.br', 'password': 'lakdj21', 'expired': True}
>>> user.get('asasas')
>>> teste = user.get('asasas')
>>> teste
>>> type(teste)
<class 'NoneType'>
>>> teste is None
True
>>> teste is not None
False
>>> if user.get('expired') is not None:
...   print(user.get('expired')
...
...
... )
...
True
>>> if not user.get('expired'):
...   print('qualquer coisa')
```

- Style guide para Python: https://www.python.org/dev/peps/pep-0008/

# Funções

- Type hints: https://www.python.org/dev/peps/pep-0484/

```python
>>> soma = lambda n1,n2: n1 + n2
>>> type(soma)
<class 'function'>
>>> soma(1,2)
3
>>> soma = lambda n1,n2: n1 / n2 if n2 != 0 else "Nao dividiras por zero!"
>>> # ternary -> expr caso verdadeiro if condicao else expr caso falso
>>> dividir = lambda n1,n2: n1 / n2 if n2 != 0 else "Nao dividiras por zero!"
>>> dividir(10,0)
'Nao dividiras por zero!'
>>> lista = [x for x in range(100)]
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> filter(lambda x: x % 2 == 0, lista)
<filter object at 0x7fb37d3fb130>
>>> list(filter(lambda x: x % 2 == 0, lista))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> # funçoes como um argumento -> function as 1st citizen class
>>> list(map(lambda x: x * x, lista))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116
, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225,
7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
>>> [ x * x for x in lista ]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116
, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225,
7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
>>> [ x for x in lista if x % 2 == 0 ]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> filtrado = filter(lambda x: x % 2 == 0, lista)
>>> filtrado
<filter object at 0x7fb37d3fb130>
>>> # lazy evaluation
>>> next(filtrado)
0
>>> next(filtrado)
2
>>> next(filtrado)
4
>>> next(filtrado)
6
>>> next(filtrado)
8
>>> next(filtrado)
10
>>> next(filtrado)
12
>>> # map, filter, reduce | comprehensions <- Guido van Rossum

>>> dic = { 'n1': 10, 'n2': 20 }
>>> soma_a_partir_de_keywords(**dic)
{'n1': 10, 'n2': 20}
dict_keys(['n1', 'n2'])
>>> # spread
>>> tupla = (1,2,3,4)
>>> soma_com_multiplos_argumentos(*tupla)
(1, 2, 3, 4)
<class 'tuple'>
1
10
```

```python
>>> def soma(x,y):
...   """
...     Recebe dois numeros inteiros e retorna a soma entre eles
...     Argumentos:
...       x: int -> primeiro numero da soma
...       y: int -> segundo numero da soma
...     Output:
...       int
...   """
...   return x + y
...
>>> help(soma)
```

# Módulos e pacotes

```bash
$ python3 -m virtualenv env
$ pip freeze
$ pip install –r "requirements.txt"
$ deactivate
```

- Alternativa ao pip: https://python-poetry.org/

## Módulos úteis

# Arquivos

```text
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
========= ===============================================================
```

```python
>>> buffer
<_io.TextIOWrapper name='arquivo.txt' mode='rt' encoding='UTF-8'>
>>> buffer.
buffer.buffer          buffer.detach(         buffer.fileno(         buffer.line_buffering  buffer.newlines        buffer.readline(       buffer.seek(           buffer.truncate(       buffer.write_through
buffer.close(          buffer.encoding        buffer.flush(          buffer.mode            buffer.read(           buffer.readlines(      buffer.seekable(       buffer.writable(       buffer.writelines(
buffer.closed          buffer.errors          buffer.isatty(         buffer.name            buffer.readable(       buffer.reconfigure(    buffer.tell(           buffer.write(
>>> conteudo = buffer.read()
>>> conteudo
'nome;idade;cidade;estado\njoao;34;osasco;SP\nfelipe;23;campinas;SP\nnadia;45;recife;PE\n'
>>> conteudo.strip().split(';')
['nome', 'idade', 'cidade', 'estado\njoao', '34', 'osasco', 'SP\nfelipe', '23', 'campinas', 'SP\nnadia', '45', 'recife', 'PE']
>>> buffer.close()

>>> conteudo
['nome;idade;cidade;estado\n', 'joao;34;osasco;SP\n', 'felipe;23;campinas;SP\n', 'nadia;45;recife;PE\n']
>>> conteudo[1].strip().split(';')
['joao', '34', 'osasco', 'SP']
>>> conteudo[2].strip().split(';')
['felipe', '23', 'campinas', 'SP']
>>> conteudo[3].strip().split(';')
['nadia', '45', 'recife', 'PE']

>>> import json
>>> with open("arquivo.json") as f:
...   conteudo = json.load(f)
...
>>> conteudo
[{'chave': 'valor'}, {'outra_chave': 11}]
>>> type(conteudo)
<class 'list'>
>>> type(conteudo[0])
<class 'dict'>
>>> type(conteudo[0].get('chave'))
<class 'str'>

>>> dic = { chr(x): x for x in range(65, 65+26) }
>>> output = [dic for x in range(10)]
>>> with open('log.json', 'x') as fp:
...   json.dump(output, fp)
...

```

```bash
$ pip install pyyaml
```

```python
>>> import yaml
>>> with open('config.yml') as fp:
...   config = yaml.safe_load(fp)
...
>>> config
{'chave': 'valor', 'campo': ['lista', 'de', 'itens'], 'pessoa': {'nome': 'Guilherme', 'idade': 33, 'estado': 'SP'}}
>>> with open('novo_arquivo.yml', 'x') as fp:
...   yaml.dump(config, fp)
...
>>>
```

- buffer.readline
  - Lê uma linha do arquivo por vez
- buffer.readlines
  - Retorna a lista de linhas

# Python para APIs

```bash
$ pip install requests
```

```python
>>> import requests
>>> requests.get("http://viacep.com.br/ws/06223040/json")
<Response [200]>
>>> import requests
>>> requests.get("https://uol.com.br/naoexite")
<Response [404]>
>>> resposta = requests.get("http://viacep.com.br/ws/06223040/json")
>>> type(resposta)
<class 'requests.models.Response'>
>>> resposta.status_code
200
>>> resposta.json()
{'cep': '06223-040', 'logradouro': 'Rua São José do Rio Pardo', 'complemento': '', 'bairro': 'Rochdale', 'localidade': 'Osasco', 'uf': 'SP', 'ibge': '3534401', 'gia': '4923', 'ddd': '11', 'siafi': '6789'}
>>> resposta.url
'http://viacep.com.br/ws/06223040/json'
>>> resposta.close()
```

- https://datatracker.ietf.org/doc/html/rfc7807
- https://datatracker.ietf.org/doc/html/rfc7807

# Testes

TDD -> Test Driven Development

testes automatizados -> unitarios / aceitacao / integracao | testes de seguranca | testes de performance -> versiona a aplicacao

# OOP

- É possível criar um novo atributo para o objeto em tempo de execução
- Validação de dados: https://pydantic-docs.helpmanual.io/
