#Validando senhas de ao menos 8 dígitos que contenham letras maiúsculas, minúsculas, números e caracteres especiais
import re
string = """
VÁLIDAS
iNBx1y6;2I#^
JTpw|X8\2n9_
86mHb~sM-O5:
?\6MpN 6nb9X
3]F`bB2_9klT

SEM MINÚSCULAS
9[W(73AZB>]7
=6KO_PS)"220
X246&JV8@R|]
ZX\M4>*56:4L
4!^PQR5A06)[

SEM MINÚSCULAS E NÚMEROS
:NPYE:|^I#Z_
WS()}>#QWM{A
KJYQ/H-G{=&_
R-K_CS@:=AQ_
`[DTK>HCU?{~

SEM NÚMEROS CARACTERES E MINÚSCULAS
JGMPCWYBVTTF
TBMIYCJCXBSR
FEDPPBTEPOKP
EFGATSYGVVFD
RDQAOEFKHATX

QUANTIDADE INVÁLIDA (6)
Wr5t7*
_0Hk3q
J4u6e~
65]riX
n0o=0I
"""
regex = re.compile(r'''
    ^
    (?=.+[A-Z])             # Verifica se há ao menos uma letra maiúscula
    (?=.+[a-z])             # Verifica se há ao menos uma letra minúscula
    (?=.+[0-9])             # Verifica se há ao menos um dígito
    (?=.+[ -\/:-@[-`{-~])   # Verifica se há ao menos um caracter especial
    .{8,}
    $
''',flags=re.M|re.X)

print(regex.findall(string))