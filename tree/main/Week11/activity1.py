import unittest

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    return a % b

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(minus(-1, 1), -2)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(9, 0), 3)
        self.assertEqual(modulus(11, 3), 2)

if __name__ == '__main__':
    unittest.main()