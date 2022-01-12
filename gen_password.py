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

categories = {
    'upper': string.ascii_uppercase,
    'lower': string.ascii_lowercase,
    'digit': string.digits,
    'punct': string.punctuation
}

def random_char(category): return random.choice(categories[category])

# Global variables
MIN_UPPER = 2
MIN_LOWER = 2
MIN_DIGIT = 2
MIN_PUNCT = 2

class PasswordGenerator(object):
    '''
    Simple password generator
    '''
    choices = ('upper', 'lower', 'digit', 'punct')

    def __init__(self):
        self.password = []
        self.counters = {
            'upper': 0,
            'lower': 0,
            'digit': 0,
            'punct': 0
        }
    
    def isValid(self):
        return self.counters['upper'] >= MIN_UPPER \
                and self.counters['lower'] >= MIN_LOWER \
                and self.counters['digit'] >= MIN_DIGIT \
                and self.counters['punct'] >= MIN_PUNCT

    def generate(self):
        """
        Generate password based 
        """
        while not self.isValid():
            choice = random.choice(self.choices)
            self.counters[choice] += 1
            self.password.append(random_char('upper'))
           
        secure_password = ''.join(self.password)        
        return secure_password

if __name__ == '__main__':
    g = PasswordGenerator()
    p = g.generate()
    print('Password : {} length={}'.format(p, len(p)))