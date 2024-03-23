# cmdkey

> Create, show, and delete stored user names and passwords.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>.

- List all user credentials:

`cmdkey /list`

- Store credentials for a user that accesses a server:

`cmdkey /add:{{server_name}} /user:{{user_name}}`

- Delete credentials for a specific target:

`cmdkey /delete {{target_name}}`
