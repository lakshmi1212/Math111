# Math Operations

This repository provides basic math operations (addition and subtraction) with production-quality tests and CI/CD integration instructions.

## Usage

```
from src.math_operations import add, subtract
result = add(2, 3)
print(result)
```

## Testing

All tests are in the `tests/` folder. Run tests using:

```
pytest tests/
```

## CI/CD

See `.github/workflows/ci.yml` for the pipeline configuration.
