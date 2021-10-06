# query

> Displays information about user sessions and process.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/query>.

- Display current user sessions:

`query session`

- Display current user sessions on a remote computer:

`query session /server:{{hostname}}`

- Display logged in users:

`query user`

- Display logged in users on a remote computer:

`query session /server:{{hostname}}`

- Display running processes:

`query process`

- Display running processes by session or user name:

`query process {{session_name|user_name}}`
