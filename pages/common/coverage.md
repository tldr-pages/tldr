# coverage

> Analyzes and measures code coverage of Python programs.
> More information: <https://coverage.readthedocs.io/en/latest/>.

- Run a test file and measure coverage:

`coverage run {{path/to/test_file.py}}`

- Run pytest tests and measure coverage:

`coverage run -m pytest {{path/to/test_file.py}}`

- Report coverage statistics for the measured code:

`coverage report`

- Generate an HTML coverage report:

`coverage html`

- Generate an XML coverage report (useful for CI pipelines):

`coverage xml`

- Show lines missing coverage in the terminal:

`coverage report --show-missing`

- Combine coverage data from multiple runs:

`coverage combine {{path/to/file1}} {{path/to/file2}}`

- Erase all previous coverage data:

`coverage erase`
