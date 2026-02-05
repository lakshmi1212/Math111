# Math Operations

This repository provides basic math operations (addition and subtraction) as Python functions, along with automated tests and CI workflow integration.

## Usage

```
from src.math_operations import add, subtract

result1 = add(2, 3)         # 5
result2 = subtract(5, 2)    # 3
```

## Testing

Install dependencies and run tests:

```
pip install -r default/requirements.txt
pytest tests/
```

## CI/CD

A GitHub Actions workflow is expected at `.github/workflows/ci.yml` to run tests automatically on push and pull requests.
