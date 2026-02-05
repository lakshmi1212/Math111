# Math111

This repository provides basic math operations (addition and subtraction) with automated tests and CI workflow integration.

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Testing

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/ -v --tb=short
```

## CI Workflow

- Workflow file: `.github/workflows/ci.yml`
- Runs tests on push and pull request to main and workflow folders

## Project Structure

- src/math_operations.py : Business logic
- tests/test_add.py : Addition tests
- tests/test_subtract.py : Subtraction tests
- default/requirements.txt : Dependencies
- default/README.md : Usage & workflow instructions
- default/math.json : CI meta data
