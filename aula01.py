import re

# re.findall() Todas as ocorrências da expressão
# re.search() Primeira ocorrência e retornar seu índice, retornando o objeto match
# re.sub() Substitui algo no texto
# re.compile() Compila expressões regulares, caso queira reutilizar
# Teste != teste



string = 'Este é um teste de expressões regulares.'

print(re.findall(r'teste', string))
print(re.search(r'teste', string))
print(re.search(r'e', string))
print(re.sub(r'teste', 'Teste', string, count=1))
print(re.sub(r'e', 'E', string, count=2))

regexp = re.compile(r'teste')

print(regexp.findall(string))
print(regexp.search(string))
print(regexp.sub('Teste', string, count=1))