# del

> Delete one or more files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Delete one or more space-separated files or patterns:

`del {{path/to/file}}`

- Prompt for confirmation before deleting each file:

`del {{path/to/file}} /p`

- Force the deletion of read-only files:

`del {{path/to/file}} /f`

- Recursively delete file(s) from all subdirectories:

`del {{path/to/file}} /s`

- Do not prompt when deleting files based on a global wildcard:

`del {{path/to/file}} /q`

- Display the help and list available attributes:

`del /?`

- Delete files based on specified attributes:

`del {{path/to/file}} /a {{attribute}}`
