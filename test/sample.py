"""This is a sample module to test the check of visium coding standards.
To test the workflow we run the ci.yml. This module is some dummy python code to make sure the CI works. """


def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""
    return a + b


def greet(name: str) -> str:
    """Print a greeting message."""
    print(f"Hello, {name}!")


def get_even_numbers(n: int) -> list[int]:
    """Return a list of even numbers up to a given limit."""
    return [num for num in range(1, n + 1) if num % 2 == 0]


def get_long_sentence() -> str:
    """Return a very long sentence."""
    long_sentence = (
        "This is a very long sentence that demonstrates how a single line of code can become"
        + "excessively long and may require line breaks or other techniques to improve readability and maintainability."
    )
    return long_sentence


def main() -> None:
    """Main function."""
    # Example usage:
    result = calculate_sum(5, 3)
    print("Sum:", result)

    greet("Alice")

    numbers = get_even_numbers(10)
    print("Even numbers:", numbers)
