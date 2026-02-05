# Math111

This repository provides basic math operations with automated testing and CI integration.

## Features
- Addition and subtraction functions
- Comprehensive pytest-based test suite
- GitHub Actions-ready workflow metadata

## Usage

```
from src.math_operations import add, subtract

print(add(3, 5))        # 8
print(subtract(10, 4))  # 6
```

## Running Tests

Ensure dependencies are installed:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/ -v --tb=short
```

## CI/CD Integration

Workflow metadata is provided in `default/math.json` for downstream automation.
