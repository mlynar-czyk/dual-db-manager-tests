"""Pytest configuration and fixtures."""
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "test": True,
        "data": [1, 2, 3, 4, 5]
    }


@pytest.fixture
def mock_environment(monkeypatch):
    """Mock environment variables."""
    monkeypatch.setenv("TEST_ENV", "true")
    monkeypatch.setenv("DEBUG", "false")
    return monkeypatch