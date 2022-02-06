# doctl auth

> Authenticate doctl with one or more API tokens.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/auth/>.

- Open a prompt to enter an API token and label its context:

`doctl auth init --context {{token_label}}`

- List authentication contexts (API tokens):

`doctl auth list`

- Switch contexts (API tokens):

`doctl auth switch --context {{token_label}}`

- Remove a stored authentication context (API token):

`doctl auth remove --context {{token_label}}`

- Show available commands:

`doctl auth --help`
