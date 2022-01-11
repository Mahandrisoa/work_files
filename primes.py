def find_primes(n):
    '''Find all prime number in a range of n given number
    '''
    primes = []
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)
    return primes

def is_prime(n):
    '''Return if number is prime or not'''
    for i in range(2, n):
        if i != n and n % i == 0:
            return False
    return True

answer = int(input('Enter N ? : '))
list = find_primes(answer)
print(list)