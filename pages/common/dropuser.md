# dropuser

> Remove an existing PostgreSQL user (role).
> More information: <https://www.postgresql.org/docs/current/app-dropuser.html>.

- Prompt for confirmation and the username before user removal:

`dropuser {{[-i|--interactive]}}`

- Remove user instantly:

`dropuser {{username}}`

- No error if the user to be removed doesn't exist:

`dropuser --if-exists {{username}}`

- Remove a user on the server with address 127.0.0.1 on port 4321:

`dropuser -h 127.0.0.1 -p 4321 {{username}}`

- Remove a user on the server with address 127.0.0.1 on port 4321 as user "admin" :

`dropuser --username=admin --host=127.0.0.1 --port=4321 {{username}}`
