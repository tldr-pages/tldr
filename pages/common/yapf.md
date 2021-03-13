# yapf

> Python style guide checker.
> More information: <https://github.com/google/yapf>.

- Display a diff of the changes that would be made, without making them (dry-run):

`yapf --diff {{path/to/file}}`

- Format the file in-place and display a diff of the changes:

`yapf --diff --in-place {{path/to/file}}`

- Recursively format all Python files in a directory, concurrently:

`yapf --recursive --in-place --style {{pep8}} --parallel {{path/to/directory}}`
