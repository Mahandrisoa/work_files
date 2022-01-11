def find_primes(n: int) -> list[int]:
    '''Find all prime number in a range of n given number
    '''
    return [i for i in range(2, n+1) if is_prime(i)]

def is_prime(n: int) -> bool:
    '''Return if number is prime or not'''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    # get input from user
    answer = int(input('Enter N ? : '))
    print(find_primes(answer))
    