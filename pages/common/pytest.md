# pytest

> Run Python tests.
> More information: <https://docs.pytest.org/en/latest/how-to/usage.html>.

- Run tests from specific files:

`pytest {{path/to/test_file1.py path/to/test_file2.py ...}}`

- Run tests with names matching a specific [k]eyword expression:

`pytest -k {{expression}}`

- Exit as soon as a test fails or encounters an error:

`pytest {{[-x|--exitfirst]}}`

- Run tests matching or excluding markers:

`pytest -m {{marker_name1 and not marker_name2}}`

- Run until a test failure, continuing from the last failing test:

`pytest {{[--sw|--stepwise]}}`

- Run tests without capturing output:

`pytest {{[-s|--capture=no]}}`

- Run tests with increased verbosity, displaying individual test names:

`pytest {{[-v|--verbose]}}`
