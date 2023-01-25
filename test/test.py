"""Contains python functions to be checked by the CI defined in check-python-style."""


def test_function(data: int) -> str:
    """This is a test function."""
    print("Hello world!")
    data = str(data)
    return data
