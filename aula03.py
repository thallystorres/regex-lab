#Quantificadores
# Metachars: ^
# * -> 0 ou n repetições
# + -> 1 ou n repetições
# ? -> 0 ou 1 repetições
# {n} -> n vezes 
# {n, } -> n ou mais vezes
# {,n } -> de 0 a n
# {min,max} -> de min a max vezes
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

texto2 = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Jã, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'Jo+ãO+', texto, flags=re.I))
print(re.findall(r'Jo*ã*+', texto2, flags=re.I))
print(re.sub(r'Jo+ãO+', 'Felipe', texto, flags=re.I))
print(re.sub(r'Jo{,1}ãO', 'Felipe', texto, flags=re.I))
print(re.sub(r've{3}m{,2}', 'Felipe', texto, flags=re.I))

texto3 = 'João ama ser amado'
print(re.findall(r'ama[do]*', texto3, flags=re.I))