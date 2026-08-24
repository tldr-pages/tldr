# yapf

> Python style guide checker.
> More information: <https://github.com/google/yapf#usage>.

- Display a diff of the changes that would be made, without making them (dry-run):

`yapf {{[-d|--diff]}} {{path/to/file}}`

- Recursively format all Python files in a directory, concurrently:

`yapf {{[-ri|--recursive --in-place]}} --style {{pep8}} {{[-p|--parallel]}} {{path/to/directory}}`
