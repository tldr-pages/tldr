# adduser

> User addition utility.

- Create a new user with a default home directory and prompts the user to set a password:

`adduser {{name}}`

- Create a new user without a home directory:

`adduser --no-create-home {{name}}`

- Create a new user with a home directory at the specified path:

`adduser --home {{path/to/home}} {{name}}`

- Create a new user with the specified shell set as the login shell:

`adduser --shell {{path/to/shell}} {{name}}`

- Create a new user belonging to the specified group:

`adduser --ingroup {{group}} {{name}}`
