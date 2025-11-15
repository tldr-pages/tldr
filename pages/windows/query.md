# query

> Display information about user sessions and process.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- Display all user sessions:

`query session`

- Display the current user sessions on a remote computer:

`query session /server:{{hostname}}`

- Display logged in users:

`query user`

- Display all user sessions on a remote computer:

`query session /server:{{hostname}}`

- Display all running processes:

`query process`

- Display running processes by session or user name:

`query process {{session_name|user_name}}`
