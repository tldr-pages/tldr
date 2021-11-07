# pylint

> A Python code linter.
> More information: <https://pylint.pycqa.org/en/latest/>.

- Show lint errors in a file:

`pylint file`

- Lint a file and use a configuration file (usually named `pylintrc`):

`pylint --rcfile {{path/to/pylintrc}} {{path/to/file.py}}`

- Disable a specific error code:

`pylint -d error_code file`
