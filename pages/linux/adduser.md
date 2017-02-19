# adduser

> User addition utility.

- Create a new user with a default home directory and prompts the user to set a password:

`adduser {{name}}`

- Create a new user without a home directory and prompts the user to set a password:

`adduser --no-create-home {{name}}`

- Create a new user with a home directory at the specified path and prompts the user to set a password:

`adduser --home {{path}} {{name}}`

- Create a new user with a default home directory, the specified shell, and prompts the user to set a password:

`adduser --shell {{path}} {{name}}`

- Create a new user belonging to the specified group with a default home directory and prompts the user to set a password:

`adduser --ingroup {{group}} {{name}}`
