# flake8

> Tool to check the style and quality of Python code.
> More information: <https://flake8.pycqa.org/>.

- Lint a file or directory recursively:

`flake8 {{path/to/file_or_directory}}`

- Show the line on which each error occurred:

`flake8 --show-source {{path/to/file_or_directory}}`

- Ignore a list of rules. (All available rules can be found at flake8rules.com):

`flake8 --ignore {{rule1,rule2}} {{path/to/file_or_directory}}`

- Exclude files matching the given globs or substrings:

`flake8 --exclude {{substring1,glob2}} {{path/to/file_or_directory}}`
