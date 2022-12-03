# black

> A Python auto code formatter.
> More information: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Auto-format a file or entire directory:

`black {{path/to/file_or_directory}}`

- Format the code passed in as a string:

`black -c "{{code}}"`

- Output whether a file or a directory would have changes made to them if they were to be formatted:

`black --check {{path/to/file_or_directory}}`

- Output changes that would be made to a file or a directory without performing them (dry-run):

`black --diff {{path/to/file_or_directory}}`

- Auto-format a file or directory, emitting exclusively error messages to `stderr`:

`black --quiet {{path/to/file_or_directory}}`

- Auto-format a file or directory without replacing single quotes with double quotes (adoption helper, avoid using this for new projects):

`black --skip-string-normalization {{path/to/file_or_directory}}`
