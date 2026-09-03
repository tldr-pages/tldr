# createuser

> Create a PostgreSQL user (role).
> More information: <https://www.postgresql.org/docs/current/app-createuser.html>.

- Create a user interactively:

`createuser {{username}} --interactive`

- Create a user with no special rights:

`createuser {{username}}`

- Create a superuser:

`createuser {{username}} {{[-s|--superuser]}}`

- Create a user allowed to create databases, manage roles, and prompt for a password:

`createuser {{username}} {{[-d|--createdb]}} {{[-r|--createrole]}} {{[-P|--pwprompt]}}`

- Create a user without the ability to create databases or manage roles:

`createuser {{username}} {{[-D|--no-createdb]}} {{[-R|--no-createrole]}}`
