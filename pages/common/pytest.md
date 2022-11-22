# pytest

> Run Python tests.
> More information: <https://docs.pytest.org/>.

- Run tests from a specific file:

`pytest {{path/to/test_file.py}}`

- Run all tests with a name that matches a given substring:

`pytest -k {{substring}}`

- Stop after the first test failure:

`pytest --exitfirst`

- Run tests matching or excluding markers:

`pytest -m {{marker_name1 and not marker_name2}}`

- Run until a test failure, continuing from the last failing test:

`pytest --stepwise`

- Run tests without capturing output:

`pytest --capture=no`
