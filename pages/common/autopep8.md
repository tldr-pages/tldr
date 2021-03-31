# autopep8

> Automatically formats Python code to confrom to the PEP 8 style guide.
> More information: <https://github.com/hhatto/autopep8>.

- Format a file to stdout, with a custom maximium line length:

`autopep8 {{path/to/file}} --max-line-length {{len}}`

- Format a file, displaying a diff of the changes:

`autopep8 --diff {{path/to/file}}`

- Format a file in-pace:

`autopep8 --in-place {{path/to/file}}`

- Format the files in-pace recursivly in dir:

`autopep8 --in-place --recursive {{path/to/dir}}`
