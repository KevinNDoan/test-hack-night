def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    Raises ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent


def square_root(n: float) -> float:
    """
    Calculate the square root of a number.
    Raises ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.5


if __name__ == "__main__":
    # Example usage
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2^3 = {power(2, 3)}")
    print(f"√16 = {square_root(16)}")
