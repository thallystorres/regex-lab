#Shorthands
# \w -> [a-zA-Z0-9À-ú_] (também apenda caracteres em madarim, kanjis, hiragana etc etc)
# \w + re.A -> [a-zA-Z0-9_] em python (se comporta exatamente como no JS)
# \W -> [^a-zA-Z0-9À-ú_]
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> (borda) basicamente é usada para localizar palavras com sufixos ou prefixos específicos
# Ex: r'\be\w+' captura ocorrência de palavras que iniciam com e
# Ex: r'\w+ e\b' captura ocorrência de palavras que terminam com e
# Ex: r'\b\w{n}\b' captura ocorrência de palavras que tenham n letras
# \B -> (não borda)
import re
texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú_]+', texto))
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\w+', texto, flags=re.A))
# print(re.findall(r'\W+', texto))
# print(re.findall(r'\d+', texto))
# print(re.findall(r'\D+', texto))
# print(re.findall(r'\s+', texto))
# print(re.findall(r'\S+', texto))
# print(re.findall(r'\be\w+', texto))
# print(re.findall(r'\w+e\b', texto))
# print(re.findall(r'\b\w{4}\b', texto))
# print(re.findall(r'\w{4}', texto))
