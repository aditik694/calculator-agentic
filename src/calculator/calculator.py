"""Core arithmetic operations for the calculator package.

Each function performs a single operation on two numeric operands.
Division by zero is handled explicitly by raising ``ZeroDivisionError``
with a clear message.
"""


def add(a: float, b: float) -> float:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference ``a - b``."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient ``a / b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
