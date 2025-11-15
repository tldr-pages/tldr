# takeown

> Take ownership of a file or directory.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- Take ownership of the specified file:

`takeown /f {{path\to\file}}`

- Take ownership of the specified directory:

`takeown /d {{path\to\directory}}`

- Take ownership of the specified directory and all subdirectories:

`takeown /r /d {{path\to\directory}}`

- Change ownership to the Administrator group instead of the current user:

`takeown /a /f {{path\to\file}}`
