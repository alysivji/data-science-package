# Data Science Package

This is an sample repository that demonstrates how to package data science code for reuse.

* code goes in the `data_science_package` folder.
* corresponding tests should be in the `tests` folder.

## Tests

Tests for our package go in `/tests/`.

This folder's file structure should mirror the structure of our package folder. File names will have to: start with "test_" or end with "_test.py" so they can be discovered by the test runner.

* Local plugins can be placed in `conftest.py`
* [Conventions for Python test discovery](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)
