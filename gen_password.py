# Generate a random password
#
# length >= 8
# >= 2 uppercases
# >= 2 lowercases
# >= 2 numbers
# >= punctuations
# at least on number

import random
import string

password = []

def random_upper(): return random.choice(string.ascii_uppercase)
def random_lower(): return random.choice(string.ascii_lowercase)
def random_digit(): return random.choice(string.digits)
def random_punctu(): return random.choice(string.punctuation)

n_upper = n_lower = n_digit = n_punct = 0
ok = False
while not ok:
    choice = random.randint(1, 4)
    print(choice)
    if choice == 1:
        n_upper += 1
        password.append(random_upper())
    elif choice == 2:
        n_lower += 1
        password.append(random_lower())
    elif choice == 3:
        n_digit += 1
        password.append(random_digit())
    elif choice == 4:
        n_punct += 1
        password.append(random_punctu())

    ok = n_upper >= 2 and n_lower >= 2 and n_digit >= 2 and n_punct >= 2
    if ok:
        break

secure_password = ''.join(password)
print('Password : {} length={}'.format(secure_password, len(secure_password)))