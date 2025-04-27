# yapf

> Python style guide checker.
> More information: <https://github.com/google/yapf>.

- Display a diff of the changes that would be made, without making them (dry-run):

`yapf {{[-d|--diff]}} {{path/to/file}}`

- Format the file in-place and display a diff of the changes:

`yapf {{[-d|--diff]}} {{[-i|--in-place]}} {{path/to/file}}`

- Recursively format all Python files in a directory, concurrently:

`yapf {{[-r|--recursive]}} {{[-i|--in-place]}} --style {{pep8}} {{[-p|--parallel]}} {{path/to/directory}}`
