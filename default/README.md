# Math111

## Overview
This repository provides basic math operations (addition & subtraction) implemented in Python, along with comprehensive pytest-based test coverage and CI/CD workflow integration.

## Usage

### Math Operations
```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

### Running Tests
Install dependencies:
```bash
pip install -r default/requirements.txt
```
Run all tests:
```bash
pytest tests/ -v --tb=short
```

## CI/CD Workflow
A GitHub Actions workflow is expected at `.github/workflows/ci.yml` to automate testing on each push and pull request.

## Folder Structure
- src/: Business logic (math_operations.py)
- tests/: Pytest test files
- default/: Metadata, requirements, and documentation

## Requirements
See `default/requirements.txt` for dependencies.
