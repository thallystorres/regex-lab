#Flags
# re.I -> IGNORECASE -> CaseInsensitive
# re.A -> re.ASCII -> Transforma tudo em ASCII
# re.M -> MULTILINE -> ^ $
# re.S -> DOTALL
import re

texto = '''
131.768.460-53a
055.134.060-50b
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))

texto2 = 'O joão gosta de folia \n E adora ser amado'

print(re.findall(r'^O.*o$' ,texto2, flags=re.I | re.S))