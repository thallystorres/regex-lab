import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''
# Positive lookahead
# ?= -> verifica se os caracteres analisados em frente condizem com o que vem a seguir
# pprint(re.findall(r'\w+\s+(\d{3}\.\d{3}\.\d\.\d)\s+\w+\s+(?=active)', texto, flags=re.M))

# Negative lookahead
# ?! -> verifica se os caracteres analisados em frente não condizem com o que vem a seguir

# pprint(re.findall(r'\w+\s+(\d{3}\.\d{3}\.\d\.\d)\s+\w+\s+(?!inactive)', texto, flags=re.M))
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind
# '(?<=)' -> verifica se os caracteres analisados atrás condizem com o que vem a seguir
# pprint(re.findall(r'\w+(?<=online)\s+(\d{3}\.\d{3}\.\d\.\d)\s+\w+\s+(?=active)', texto, flags=re.M|re.I))

# Negative lookbehind
# '(?<!)' verifica se os caracteres analisados atrás não condizem com o que vem a seguir
# pprint(re.findall(r'\w+(?<!online)\s+(\d{3}\.\d{3}\.\d\.\d)\s+\w+\s+(?=active)', texto, flags=re.M|re.I))