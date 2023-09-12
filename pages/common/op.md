# op

> Official CLI for 1Password's desktop app.
> More information: <https://developer.1password.com/docs/cli>.

- Sign in to a 1Password account:

`op signin`

- List all vaults:

`op vault list`

- Print item details in JSON format:

`op item get {{item_name}} --format json`

- Create a new item with a category in the default vault:

`op item create --category {{category_name}}`

- Print a referenced secret in `stdout`:

`op read {{secret_reference}}`

- Pass secret references from exported environment variables to a command:

`op run -- {{command}}`

- Pass secret references from an environment file to a command:

`op run --env-file {{path/to/env_file.env}} -- {{command}}`

- Read secret references from an input file and save plaintext secrets to an output file:

`op inject -i {{path/to/input_file}} -o {{path/to/output_file}}`
