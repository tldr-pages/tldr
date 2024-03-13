# isort

> Sort Python import statements alphabetically within sections and by type.
> It can be run on multiple files or an entire project, simplifying import management.
> More information: <https://pycqa.github.io/isort/>.

- Sort imports in one or more Python files, modifying them in-place:

`isort {{path/to/file1.py path/to/file2.py ...}}`

- Show the changes `isort` would make without applying them:

`isort --check-only {{path/to/file.py}}`

- Apply changes `isort` would make, displaying the differences:

`isort --diff {{path/to/file.py}}`

- Exclude files or directories from being sorted. If you want to skip multiple files you should specify --skip twice:

`isort --skip {{path/to/file1}} --skip {{path/to/directory1}}`

- Show verbose output, such as when files are skipped or when a check is successful:

`isort --verbose`

- Display [h]elp:

`isort --help`

- Display [v]ersion:

`isort --version`
