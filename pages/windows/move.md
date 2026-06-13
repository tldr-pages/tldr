# move

> Move or rename files and directories.
> In PowerShell, this command is an alias of `Move-Item`. This documentation is based on the Command Prompt (`cmd`) version of `move`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/move>.

- View documentation of the equivalent PowerShell command:

`tldr move-item`

- Rename a file or directory when the target is not an existing directory:

`move {{path\to\source}} {{path\to\target}}`

- Move a file or directory into an existing directory:

`move {{path\to\source}} {{path\to\existing_directory}}`

- Move a file or directory across drives:

`move {{C:\path\to\source}} {{D:\path\to\target}}`

- Do not prompt for confirmation before overwriting existing files:

`move /Y {{path\to\source}} {{path\to\existing_directory}}`

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`move /-Y {{path\to\source}} {{path\to\existing_directory}}`
