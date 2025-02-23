def calculate_fibonacci(n: int) -> list[int]:
    """Calculate the first n numbers in the Fibonacci sequence."""
    if n <= 0:
        return []

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def main():
    # Example usage of the Fibonacci calculator
    num_terms = 10
    result = calculate_fibonacci(num_terms)
    print(f"First {num_terms} Fibonacci numbers:")
    print(result)


if __name__ == "__main__":
    main()
