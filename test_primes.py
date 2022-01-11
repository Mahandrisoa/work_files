import unittest
from primes import is_prime, find_primes 

class PrimeTest(unittest.TestCase):
    def setUp(self):
        print('Setup PrimeTest')

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        # Should raises TypeError on empty call and by passing string as parameter
        with self.assertRaises(TypeError):
            is_prime()
            is_prime('abc')

    def test_find_primes(self):
        self.assertEqual(find_primes(-2), [])
        self.assertEqual(find_primes(0), [])
        self.assertEqual(find_primes(1), [])

        self.assertEqual(find_primes(2), [2])
        self.assertEqual(find_primes(10), [2, 3, 5, 7])

    def tearDown(self):
        print('TearDown')

if __name__ == '__main__':
    unittest.main()