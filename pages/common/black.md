# black

> A Python auto code formatter.
> More information: <https://github.com/psf/black>.

- Auto-format a file or entire directory:

`black {{path/to/file_or_directory}}`

- Format the code passed in as a string:

`black -c "{{code}}"`

- Output the changes that would be applied for each file:

`black --diff {{path/to/file_or_directory}}`

- Perform a dry run (print what would be done without actually doing it):

`black --check {{path/to/file_or_directory}}`

- Auto-format a file or directory emitting exclusively error messages to stderr:

`black --quiet {{path/to/file_or_directory}}`

- Auto-format a file or directory without replacing single quotes with double quotes (adoption helper, avoid using this for new projects):

`black --skip-string-normalization {{path/to/file_or_directory}}`
