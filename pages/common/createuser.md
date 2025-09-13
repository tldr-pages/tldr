# createuser

> Create a PostgreSQL user (role).
> More information: <https://www.postgresql.org/docs/current/app-createuser.html>.

- Create a user interactively:

`createuser --interactive {{username}}`

- Create a user with no special rights:

`createuser {{username}}`

- Create a superuser:

`createuser {{[-s|--superuser]}} {{username}}`

- Create a user allowed to create databases, manage roles, and prompt for a password:

`createuser {{[-d|--createdb]}} {{[-r|--createrole]}} {{[-P|--pwprompt]}} {{username}}`

- Create a user without the ability to create databases or manage roles:

`createuser {{[-D|--no-createdb]}} {{[-R|--no-createrole]}} {{username}}`
