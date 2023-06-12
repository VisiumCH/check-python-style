def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b


def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")


def get_even_numbers(n):
    """Returns a list of even numbers up to a given limit."""
    return [num for num in range(1, n + 1) if num % 2 == 0]


def get_long_sentence():
    long_sentence = (
        "This is a very long sentence that demonstrates how a single line of code can become"
        + "excessively long and may require line breaks or other techniques to improve readability and maintainability."
    )
    return long_sentence


def main():
    # Example usage:
    result = calculate_sum(5, 3)
    print("Sum:", result)

    greet("Alice")

    numbers = get_even_numbers(10)
    print("Even numbers:", numbers)
