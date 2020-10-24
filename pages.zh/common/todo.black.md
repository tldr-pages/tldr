# black

> Pythond代码格式化工具.
> 详见: <https://github.com/psf/black>.

- 自动格式化文件或者整个目录:

`black {{path/to/file_or_directory}}`

- Format the code passed in as a string:

`black -c {{path/to/file_or_directory}}`

- Output a diff for each file on stdout:

`black --diff {{path/to/file_or_directory}}`

- Return the status without writing the files back:

`black --check {{path/to/file_or_directory}}`

- Auto-format a file or directory emitting exclusively error messages to stderr:

`black --quiet {{path/to/file_or_directory}}`
