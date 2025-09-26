mport unittest
from FarenheitFibonacci import main, farenheit_to_celsius, fibonacci

# Unit tests for the functions
class TestFunctions(unittest.TestCase):

    def test_farenheit_to_celsius(self):
        self.assertAlmostEqual(farenheit_to_celsius(32), 0)
        self.assertAlmostEqual(farenheit_to_celsius(212), 100)
        self.assertAlmostEqual(farenheit_to_celsius(98.6), 37)

    # Exception tests
    def test_fibonacci_exceptions(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(3.5)
        with self.assertRaises(ValueError):
            fibonacci("a string")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    # Exception tests
    def test_farenheit_to_celsius_exceptions(self):
        with self.assertRaises(ValueError):
            farenheit_to_celsius("a string")
        with self.assertRaises(ValueError):
            farenheit_to_celsius(None)
   
if __name__ == '__main__':
    unittest.main()
