# doctl

> Official command-line interface for the DigitalOcean API.
> More information: <https://docs.digitalocean.com/reference/doctl/>.

- Authenticate doctl with your DigitalOcean account using an API token:

`doctl auth init`

- Display the currently authenticated account information:

`doctl account get`

- List all droplets (cloud servers) in your account:

`doctl compute droplet list`

- List all Kubernetes clusters:

`doctl kubernetes cluster list`

- List all managed databases:

`doctl databases list`

- Display help for a subcommand:

`doctl {{subcommand}} --help`
