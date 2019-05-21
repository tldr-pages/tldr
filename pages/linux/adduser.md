# adduser

> User addition utility.

- Create a new user with a default home directory and prompt the user to set a password:

`adduser {{username}}`

- Create a new user without a home directory:

`adduser --no-create-home {{username}}`

- Create a new user with a home directory at the specified path:

`adduser --home {{path/to/home}} {{username}}`

- Create a new user with the specified shell set as the login shell:

`adduser --shell {{path/to/shell}} {{username}}`

- Create a new user belonging to the specified group:

`adduser --ingroup {{group}} {{username}}`

- Add an existing user to the specified group:

`adduser {{username}} {{group}}`
