import unittest
from FarenheitFibonacci import main, farenheit_to_celsius, fibonacci

# Unit tests for the functions
class TestFunctions(unittest.TestCase):

    def test_farenheit_to_celsius(self):
        self.assertAlmostEqual(farenheit_to_celsius(32), 0)
        self.assertAlmostEqual(farenheit_to_celsius(212), 100)
        self.assertAlmostEqual(farenheit_to_celsius(98.6), 37)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

# Run functions and tests
if __name__ == "__main__":
    main()
    unittest.main(argv=[''], exit=False)  # Run the tests without exiting the interpreter