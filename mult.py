def mult(x, y):
    return x * y

import unittest

class TestMult(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(mult(2, 5), 10)

    def test_mult_negativos(self):
        self.assertEqual(mult(-3,- 5),  15)

if __name__ == "__main__":
    unittest.main()