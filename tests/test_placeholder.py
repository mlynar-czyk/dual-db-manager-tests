"""Placeholder test to ensure test framework is working."""
import pytest


def test_placeholder():
    """Basic test to verify pytest is working."""
    assert True


def test_sample_data(sample_data):
    """Test using fixture."""
    assert sample_data["test"] is True
    assert len(sample_data["data"]) == 5


class TestPlaceholder:
    """Test class example."""
    
    def test_class_method(self):
        """Test method in class."""
        result = 2 + 2
        assert result == 4