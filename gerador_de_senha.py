from random import randint, choice, shuffle

def zero_a_nove():
    return chr(randint(48, 57))

def a_a_z():
    return chr(randint(97, 122))

def A_a_Z():
    return chr(randint(65, 90))

def weird_chars():
    rand_range = [
        randint(33, 47),  # \u0021-\u002f [! - /]
        randint(58, 64),  # \u003A-\u0040 [: - @]
        randint(91, 96),  # \u005B-\u0060 [[ - `]
        randint(123, 126) # \u007B-\u007E [{ - ~]
    ]

    # [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
    # [ -\/:-@[-`{-~]
    
    return chr(choice(rand_range))

def create_password(length=12, upper=True, lower=True, numbers=True, weird=True):
    if not any([upper, lower, numbers, weird]):
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")

    password = []

    for i in range(length):
        if numbers:
            password.append(zero_a_nove())
        if lower:
            password.append(a_a_z())
        if upper:
            password.append(A_a_Z())
        if weird:
            password.append(weird_chars())
    
    password = password[:length]
    shuffle(password)
    return ''.join(password)


if __name__ == '__main__':

    print('VÁLIDAS')
    for i in range(5):
        print(create_password(
            length=12,
            weird=True,
            upper=True,
            lower=True,
            numbers=True
        ))
    print()

    print('SEM MINÚSCULAS')
    for i in range(5):
        print(create_password(
            length=12,
            weird=True,
            upper=True,
            lower=False,
            numbers=True
        ))
    print()

    print('SEM MINÚSCULAS E NÚMEROS')
    for i in range(5):
        print(create_password(
            length=12,
            weird=True,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    print('SEM NÚMEROS CARACTERES E MINÚSCULAS')
    for i in range(5):
        print(create_password(
            length=12,
            weird=False,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    print('QUANTIDADE INVÁLIDA (6)')
    for i in range(5):
        print(create_password(
            length=6,
        ))
    print()