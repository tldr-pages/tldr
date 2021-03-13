# yapf

> Python style guide checker.
> More information: <https://github.com/google/yapf>.

- Print out the diff that will occur after formatting:

`yapf --diff {{path/to/file}}`

- Print out the formatted diff and make the changes in the file:

`yapf --diff --in-place {{path/to/file}}`

- Format all Python files in a directory recursivly (in pep8 style for example) in parallel:

`yapf --recursive --in-place --style pep8 --parallel {{path/to/directory}}`
