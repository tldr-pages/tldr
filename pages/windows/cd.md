# cd

> Display the current working directory or move to a different directory.
> In PowerShell, this command is an alias of `Set-Location`. This documentation is based on the Command Prompt (`cmd`) version of `cd`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- View documentation of the equivalent PowerShell command:

`tldr set-location`

- Display the path of the current directory:

`cd`

- Go to a specific directory in the same drive:

`cd {{path\to\directory}}`

- Go to a specific directory in a different [d]rive:

`cd /d {{C}}:{{path\to\directory}}`

- Go up to the parent of the current directory:

`cd ..`

- Go to the home directory of the current user:

`cd %userprofile%`

- Go to root of current drive:

`cd \`
