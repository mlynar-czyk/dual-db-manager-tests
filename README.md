# Test Repository for dual-db-manager

This repository contains automated tests for the [dual-db-manager](https://github.com/mlynar-czyk/dual-db-manager) project.

## 🤖 Automated Synchronization

This repository is automatically synchronized with the main repository:
- Source code is synced on every push
- Tests run automatically on code changes
- Coverage reports are generated and tracked
- Security scanning is integrated

## 📊 Test Coverage

Current coverage threshold: 80%

## 🧪 Running Tests Locally

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_placeholder.py
```

## 🔧 Configuration

Test configuration is managed in:
- `pytest.ini` - Pytest configuration
- `requirements-test.txt` - Test dependencies
- `.github/workflows/` - CI/CD workflows