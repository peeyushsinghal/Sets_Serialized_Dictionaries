# Dictionary Validation and Merging

This repository contains two Python modules that handle dictionary operations:

1. **Dictionary Validation** (`student_code.py`)
   - Validates nested dictionary structures against a template
   - Checks for correct types and required keys
   - Returns detailed error messages for validation failures

2. **Dictionary Merging** (`student_merge.py`)
   - Merges multiple dictionaries containing word frequencies
   - Implements two different approaches:
     - Using `collections.defaultdict`
     - Using `collections.Counter`
   - Sorts results by frequency (descending) and alphabetically

## Running Tests

The repository includes comprehensive test suites for both modules. To run the tests locally:

```bash
# Install required packages
pip install pytest

# Run validation tests
pytest test_validate.py

# Run merging tests
pytest test_merge.py

# Run all tests
pytest
```

## GitHub Actions

The repository uses GitHub Actions for continuous integration. On each push:
- Runs both test suites sequentially
- Reports test results in the Actions tab
- Fails the build if any tests fail

## Project Structure

```
.
├── student_code.py      # Dictionary validation implementation
├── student_merge.py     # Dictionary merging implementation
├── test_validate.py     # Validation tests
├── test_merge.py       # Merging tests
├── README.md           # This file
└── .github/workflows   # GitHub Actions configuration
``` 