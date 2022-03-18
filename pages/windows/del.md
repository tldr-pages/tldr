# del

> Delete one or more files. Wildcards are supported.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/del>.

- Delete the specified files:

`del {{path/to/file1 path/to/file2 ...}}`

- Force the deletion of read-only files:

`del {{path/to/file1 path/to/file2 ...}} /f`

- Prompt for the confirmation before deleting each file:

`del /p {{path/to/file1 path/to/file2 ...}}`

- Do not prompt for the confirmation before deleting each file:

`del /q {{path/to/file1 path/to/file2 ...}}`

- Delete files with the specified [a]ttributes:

`del /a {{attributes}} {{path/to/file1 path/to/file2 ...}}`

- Recur[s]ively delete files from the specified directories:

`del /s {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Print the help:

`del /?`
