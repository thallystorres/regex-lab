import re

# validador de IPv4

ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
        25[0-5]|
        2[0-4][0-9]|
        1[0-9]{2}|
        [1-9][0-9]|
        [0-9]
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))