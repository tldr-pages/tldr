# setx

> Sets persistent environment variables.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- Set an environment variable for the current user:

`setx {{variable}} {{value}}`

- Set an environment variable for the current machine:

`setx {{variable}} {{value}} /M`

- Set an environment variable for a user on a remote machine:

`setx /s {{hostname}} /u {{username}} /p {{password}} {{variable}} {{value}}`

- Set an environment variable from a registry key value:

`setx {{variable}} /k {{registry\key\path}}`
