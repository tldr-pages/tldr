# secrethub

> A tool to keep secrets out of config files.
> More information: <https://secrethub.io>.

- Print a secret to stdout:

`secrethub read {{path/to/secret}}`

- Generate a random value and store it as a new secret (version):

`secrethub generate {{path/to/secret}}`

- Store a value from the clipboard as a new secret (version):

`secrethub write --clip {{path/to/secret}}`

- Store a value supplied on stdin as a new secret (version):

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- Audit a repository or secret:

`secrethub audit {{path/to/repo_or_secret}}`
