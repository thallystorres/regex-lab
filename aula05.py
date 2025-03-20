#Grupos e retrovisores
# ()
# ()       \1
# () ()    \1  \2
# (())()   \1  \2  \3
import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
# regexppp = r'<(?P<tag>[dipv]{1,3})>(:?.+?)<\/(?P=tag)>'
# tags = re.findall(regexp, texto, flags=re.I)
# print(*tags, sep='\n')

cpf = '113.438.644-37'

regexp = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{3}$'
regexpp = r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$'
print(re.findall(regexpp, cpf))

regexppp = r'(<(.+?)>)(.+?)(</\2>)'
# print(re.findall(regexppp, texto))
print(re.sub(regexppp, r'\1\3\4', texto))