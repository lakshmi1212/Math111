# Math111

Math111 provides basic math operations: addition and subtraction.

## Usage

```
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
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
- Uses pytest for running tests in `tests/` folder.

