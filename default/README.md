# Math111

This repository provides basic math operations (addition and subtraction) and their corresponding test cases using pytest.

## Usage

Import functions from `src/math_operations.py`:
```python
from src.math_operations import add, subtract
```

## Running Tests

Install dependencies:
```bash
pip install -r default/requirements.txt
```

Run tests:
```bash
python -m pytest tests/ -v --tb=short
```

## CI Workflow

All tests are executed as part of the CI pipeline defined in `.github/workflows/ci.yml`.

---

- Source code: `src/`
- Tests: `tests/`
- Metadata: `default/math.json`
