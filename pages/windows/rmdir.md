# rmdir

> Remove a directory and its contents.
> In PowerShell, this command is an alias of `Remove-Item`. This documentation is based on the Command Prompt (`cmd`) version of `rmdir`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- View the documentation of the equivalent PowerShell command:

`tldr remove-item`

- Remove an empty directory:

`rmdir {{path\to\directory}}`

- Remove a directory and its contents recursively:

`rmdir {{path\to\directory}} /s`

- Remove a directory and its contents recursively without prompting:

`rmdir {{path\to\directory}} /s /q`
