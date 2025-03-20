import re
from pprint import pprint
# Numero de telefones
texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

regex = re.compile(r"""
    ^
    (\(\d{2}\)\s*)?     # Verificação optativa do DDD
    (9\s?)?             # Verificação optativa do dígito 9
    (\d{4}[\s-]\d{4})   # Verificação obrigatória dos 8 números separados por '-' ou ' '
    $
""", flags=re.M|re.X)

regex_bruta = re.compile(r"""
    ^
    (\(\d{2}\)\s)
    (9\s*)
    (\d{4}-\d{4})
    $
    #Aceita APENAS os formatos (84) 9 8798-8351 e (84) 98798-8351
""", flags=re.M|re.X)

pprint(regex_bruta.findall(texto))
