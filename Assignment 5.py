def main():
    # Temperature
    temp = float(input("Enter temperature in Farenheit: "))
    celsius = farenheit_to_celsius(temp)
    print(f"Temperature in Celsius: {celsius}")

    # Fibonacci
    n = int(input("Enter a non-negative integer for Fibonacci: "))
    fib_number = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {fib_number}")

# The two functions.
def farenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number")
    return (fahrenheit - 32) * 5.0 / 9.0

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
