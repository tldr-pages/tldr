# del

> Delete one or more files.
> In PowerShell, this command is an alias of `Remove-Item`. This documentation is based on the Command Prompt (`cmd`) version of `del`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- View the documentation of the equivalent PowerShell command:

`tldr remove-item`

- Delete one or more space-separated files or patterns:

`del {{file_pattern}}`

- Prompt for confirmation before deleting each file:

`del {{file_pattern}} /p`

- Force the deletion of read-only files:

`del {{file_pattern}} /f`

- Recursively delete file(s) from all subdirectories:

`del {{file_pattern}} /s`

- Do not prompt when deleting files based on a global wildcard:

`del {{file_pattern}} /q`

- Display the help and list available attributes:

`del /?`

- Delete files based on specified attributes:

`del {{file_pattern}} /a {{attribute}}`
