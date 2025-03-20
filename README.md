
# Python Regex Lab
Repositório contendo exercícios e exemplos para aprender expressões regulares (regex) em Python.

## Visão Geral
Este repositório é uma coleção de exemplos e desafios para aprender e praticar expressões regulares em Python. As aulas são divididas entre conceitos básicos, tópicos avançados e aplicações práticas, proporcionando uma compreensão sólida de como usar regex em diversas situações do mundo real.

## Índice
- [Visão Geral](#visão-geral)
- [Conceitos Básicos](#conceitos-básicos)
- [Tópicos Avançados](#tópicos-avançados)
- [Exemplos Práticos](#exemplos-práticos)
- [Aplicações no Mundo Real](#aplicações-no-mundo-real)
- [Utilitários](#utilitários)
- [Agradecimentos Especiais](#agradecimentos-especiais)

## Como Rodar os Exemplos

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuário/python-regex-lab.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd python-regex-lab
   ```

3. Execute os exemplos:
   ```bash
   python aula01.py
   ```

Certifique-se de ter o Python 3 instalado. Caso necessário, instale as dependências com:
```bash
pip install -r requirements.txt
```

## Conceitos Básicos

### **aula01.py**: Introdução aos Métodos Regex
- `re.findall()`, `re.search()`, `re.sub()`, `re.compile()`
- Correspondência básica de padrões

### **aula02.py**: Metacaracteres
- Caracteres especiais: `.`, `^`, `*`, `+`, `?`, `{}`, `[]`, `\`, `|`, `()`
- Correspondência sem distinção entre maiúsculas e minúsculas com `flags=re.I`

### **aula03.py**: Quantificadores
- `*` (0 ou mais)
- `+` (1 ou mais)
- `?` (0 ou 1)
- `{n}` (exatamente n)
- `{n,}` (n ou mais)
- `{,n}` (0 até n)
- `{min,max}` (intervalo)

## Tópicos Avançados

### **aula04.py**: Ganância vs Não-Ganância
- Correspondência gananciosa com `*` e `+`
- Correspondência não-gananciosa com `*?` e `+?`

### **aula05.py**: Grupos e Retroreferências
- Grupos de captura com `()`
- Retroreferências com `\1`, `\2`, etc.
- Grupos nomeados com `(?P<nome>)`

### **aula06.py**: Padrões de Início/Fim
- `^` - Início da linha
- `$` - Fim da linha
- `[^]` - Negação

### **aula07a.py** & **aula07b.py**: Abreviações & Flags
- `\w`, `\W`, `\d`, `\D`, `\s`, `\S`
- Limites de palavra `\b`, `\B`
- Flags: `re.I`, `re.M`, `re.S`

## Exemplos Práticos

### **aula08.py**: Lookahead/Lookbehind
- Lookahead positivo `(?=)`
- Lookahead negativo `(?!)`
- Lookbehind positivo `(?<=)`
- Lookbehind negativo `(?<!)`

### **aula09cpf.py**: Validação de CPF
- Correspondência de padrões complexos
- Validação de formato
- Validação de dígitos

### **aula09ipv4.py**: Validação de IPv4
- Validação de intervalo de números
- Verificação de formato

## Aplicações no Mundo Real

### **aula11.py**: Validação de Número de Telefone
- DDD opcional
- Diferentes formatos
- Captura de grupos

### **aula12.py**: Validação de Senha
- Comprimento mínimo
- Requisitos de tipos de caracteres
- Caracteres especiais

### **aula13.py**: Validação de Números
- Validação de inteiros
- Validação de números flutuantes
- Tratamento de sinal

### **aula14.py**: Validação de E-mails
- Conformidade com o RFC
- Padrões complexos
- Casos extremos

## Utilitários

### **gerador_de_senha.py**: Gerador de Senhas
- Comprimento personalizado
- Seleção de tipos de caracteres
- Geração aleatória

## Agradecimentos Especiais
Este repositório é parte de uma jornada de aprendizado com o mestre [Otávio Miranda](https://github.com/luizomf) e o [Curso de Expressões Regulares com Python](https://www.udemy.com/course/expressoes-regulares-com-python-3-curso-gratuito/).
