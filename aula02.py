#Metachars
# Metachars: . ^ * + ? { } [ ] \ | ( )
# \ -> Teclas de escape
# | -> OU
# . -> Qualquer caracter
# []-> Conjunto de caracteres
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

print(re.findall(r'João|Maria|ad.....', texto))
print(re.findall(r'João|joão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria|[0-9]', texto))
print(re.findall(r'[A-Za-z]aria', texto))
print(re.findall(r'jOão|mariA', texto, flags=re.I))