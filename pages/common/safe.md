# safe

> A CLI to interact with HashiCorp Vault.
> More information: <https://github.com/starkandwayne/safe>.

- Add a safe target:

`safe target {{vault_addr}} {{target_name}}`

- Authenticate the CLI client against the Vault server, using an authentication token:

`safe auth {{authentication_token}}`

- Print the environment variables describing the current target:

`safe env`

- Provide a tree hierarchy listing of all reachable keys in the Vault:

`safe tree {{path}}`

- Move a secret from one path to another:

`safe move {{old_path/secret}} {{new_path/secret}}`

- Generate a new 2048-bit SSH keypair and store it in vault:

`safe ssh 2048 {{path/secret}}`

- Set non-sensitive keys for a secret:

`safe set {{path/secret}} {{key}}={{value}}`

- Set auto-generated password in a secret:

`safe gen {{path/secret}} {{key}}`
