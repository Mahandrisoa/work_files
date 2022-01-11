import logging

my_format = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=my_format)

logger = logging.getLogger()


def find_primes(n: int) -> list[int]:
    '''
    Find all prime number in a range of n given number
    >>> is_prime(5)
    True

    :int: n: input number
    '''
    return [i for i in range(2, n+1) if is_prime(i)]

def is_prime(n: int) -> bool:
    '''
    Return if number is prime or not
    '''
    logger.info("Check if {} is prime".format(n))
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    # get input from user
    answer = input('Enter N ? : ')
    if not answer:
        logger.warning('No value given')

    logger.debug('answer', answer)

    try:
        n = int(answer)
        print(find_primes(n))
    except:
        logger.error("Wrong type for input argument N")

    