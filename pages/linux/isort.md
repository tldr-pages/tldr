# isort

> Sort Python import statements alphabetically within sections and by type.
> `isort` can be run on multiple files or an entire project, simplifying import management.
> More information: <https://pycqa.github.io/isort/>.

- Sort imports in a Python file, modifying the file in-place:

`isort {{path/to/file.py}}`

- Sort imports in multiple Python files, modifying the files in-place:

`isort {{path/to/file1.py}} {{path/to/file2.py}} ...`

- Show the changes `isort` would make without applying them:

`isort --check-only {{path/to/file.py}}`

- Apply changes `isort` would make, displaying the differences:

`isort --diff {{path/to/file.py}}`

- Recursively sort imports in all Python files within a directory:

`isort --add-import "from __future__ import division" {{path/to/file.py}}`

- Exclude files or directories from being sorted:

`isort --skip {{file_or_directory_to_skip}} {{path/to/directory}}`

- Display help:

`isort --help`

- Display version:

`isort --version`
