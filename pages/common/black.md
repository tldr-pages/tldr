# black

> A speedy Python auto code formatter.
> More information: <https://github.com/psf/black>.

- Auto-format a file or entire directory:

`black {{path/to/file_or_directory}}`

- Format the code passed in as a string:

`black -c {{path/to/file_or_directory}}`

- Output a diff for each file on stdout:

`black --diff {{path/to/file_or_directory}}`

- Don't write the files back, just return the status:

`black --check {{path/to/file_or_directory}}`

- Don't emit non-error messages to stderr:

`black --quiet {{source_file_or_directory}}`
