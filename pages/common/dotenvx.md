# dotenvx

> A better `dotenv`, from the creator of `dotenv`.
> More information: <https://dotenvx.com/docs>.

- Run a command with environment variables from a `.env` file:

`dotenvx run -- {{command}}`

- Run a command with environment variables from a specific `.env` file:

`dotenvx run -f {{path/to/file.env}} -- {{command}}`

- Set an environment variable with encryption:

`dotenvx set {{key}} {{value}}`

- Set an environment variable without encryption:

`dotenvx set {{key}} {{value}} --plain`

- Return environment variables defined in a `.env` file:

`dotenvx get`

- Return the value of an environment variable defined in a `.env` file:

`dotenvx get {{key}}`

- Return all environment variables from `.env` files and OS:

`dotenvx get --all`
