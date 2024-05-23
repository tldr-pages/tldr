# secrethub

> Keep secrets out of config files.
> More information: <https://github.com/secrethub/secrethub-cli>.

- Print a secret to `stdout`:

`secrethub read {{path/to/secret}}`

- Generate a random value and store it as a new or updated secret:

`secrethub generate {{path/to/secret}}`

- Store a value from the clipboard as a new or updated secret:

`secrethub write --clip {{path/to/secret}}`

- Store a value supplied on `stdin` as a new or updated secret:

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- Audit a repository or secret:

`secrethub audit {{path/to/repo_or_secret}}`
