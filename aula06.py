#Metachars de inicio e fim
# ^ -> Inicio de análise
# $ -> Fim de análise
# [^] -> Negação
import re

cpf = '113.438.644-37'

regexpp = r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$'
print(re.findall(regexpp, cpf))
print(re.findall(r'[^0-9a-zA-Z]+', cpf))