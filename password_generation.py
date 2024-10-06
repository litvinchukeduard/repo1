import random

from string import ascii_lowercase, ascii_uppercase, punctuation
'''
Написати функцію, яка буде генерувати випадковий пароль певної довжини
'''

# ['a', 'b', 'c', 'd', 'e']

# "abcdef"
# lowercase_letters = "abcdef"

# abdfgdfM+
# Gddff-

# 1) Скласти пароль з літер у нижньому регістрі
# 2) Додати у пароль символ у верхньому регістрі
# 3) Додати у пароль спеціальний символ
#

def generate_random_password(password_length: int) -> str:
    """ Random password generator. Accepts password length start from 3"""
    if (password_length < 3):
        raise ValueError

    password = []
    for _ in range(1, password_length - 2 + 1): # Not using i -> _
        password.append(random.choice(ascii_lowercase))
    
    # uppercase_letter = random.choice(ascii_uppercase)
    # password += uppercase_letter
    password.append(random.choice(ascii_uppercase))
    password.append(random.choice(punctuation))

    random.shuffle(password)

    return ''.join(password)

print(generate_random_password(8))
# print(generate_random_password(6))
# print(generate_random_password(3))
# print(generate_random_password(8))
print(generate_random_password(3))

# my_str = "abcde"
# my_str[1] = '1'

