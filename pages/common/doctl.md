# doctl

> Manage DigitalOcean resources.
> Some subcommands such as `auth`, `compute`, `databases`, `kubernetes`, and `serverless` have their own usage documentation.
> More information: <https://docs.digitalocean.com/reference/doctl/>.

- Authenticate with a DigitalOcean API token:

`doctl auth init`

- List all Droplets:

`doctl compute droplet list`

- List all Kubernetes clusters:

`doctl kubernetes cluster list`

- List all managed databases:

`doctl databases list`

- List all deployed apps:

`doctl apps list`

- Display account information:

`doctl account get`

- Display help for a subcommand:

`doctl {{auth|compute|databases|kubernetes|serverless}} --help`
