# safe

> Interact with HashiCorp Vault.
> More information: <https://github.com/starkandwayne/safe>.

- Add a safe target:

`safe target {{vault_addr}} {{target_name}}`

- Authenticate the CLI client against the Vault server, using an authentication token:

`safe auth {{authentication_token}}`

- Print the environment variables describing the current target:

`safe env`

- Display a tree hierarchy of all reachable keys for a given path:

`safe tree {{path}}`

- Move a secret from one path to another:

`safe move {{old/path/to/secret}} {{new/path/to/secret}}`

- Generate a new 2048-bit SSH key-pair and store it:

`safe ssh {{2048}} {{path/to/secret}}`

- Set non-sensitive keys for a secret:

`safe set {{path/to/secret}} {{key}}={{value}}`

- Set auto-generated password in a secret:

`safe gen {{path/to/secret}} {{key}}`
