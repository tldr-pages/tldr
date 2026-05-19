# where

> Display the location of files that match the search pattern.
> Defaults to current work directory and paths in the `%PATH%` environment variable.
> In PowerShell, this command is an alias for `Where-Object`. This documentation is based on the Command Prompt (`cmd`) version of `where`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- View the documentation of the equivalent PowerShell command:

`tldr where-object`

- Display the location of file pattern:

`where {{file_pattern}}`

- Display the location of file pattern including file size and date:

`where /T {{file_pattern}}`

- Recursively search for file pattern at specified path:

`where /R {{path\to\directory}} {{file_pattern}}`

- Silently return the error code for the location of the file pattern:

`where /Q {{file_pattern}}`
