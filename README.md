# Calculator

A simple, dependency-free Python calculator that supports four basic
arithmetic operations: **add**, **subtract**, **multiply**, and **divide**.

## Features

- Four operations: `add`, `subtract`, `multiply`, `divide`
- Division by zero is handled by raising a clear `ZeroDivisionError`
- No third-party runtime dependencies
- Tested with `pytest`

## Project Layout

```
src/calculator/      # Package implementation
  __init__.py        # Public API exports
  calculator.py      # Core operations
tests/               # pytest test suite
  test_calculator.py
```

## Usage

```python
from calculator import add, subtract, multiply, divide

add(2, 3)        # -> 5
subtract(5, 3)   # -> 2
multiply(2, 3)   # -> 6
divide(10, 2)    # -> 5.0
divide(1, 0)     # -> raises ZeroDivisionError
```

## Running the Tests

```bash
pytest
```

## Requirements

- Python 3.8+
- `pytest` (for running the test suite only)
