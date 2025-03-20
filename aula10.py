import re
cepefe = '025.258.963-10'

cpf = re.compile(r'^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$')
print(cpf.findall(cepefe))
