# linode-cli

> Manage Linode cloud services.
> Some subcommands such as `linodes`, `lke`, `domains`, `volumes`, and `object-storage` have their own usage documentation.
> More information: <https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli>.

- Configure the CLI with an API token:

`linode-cli configure`

- List all Linode instances:

`linode-cli linodes list`

- Create a new Linode instance:

`linode-cli linodes create --type {{linode_type}} --region {{region}} --image {{image_id}}`

- List all Kubernetes clusters:

`linode-cli lke clusters-list`

- List all domains:

`linode-cli domains list`

- List all volumes:

`linode-cli volumes list`

- Display help for a subcommand:

`linode-cli {{linodes|lke|domains|volumes}} --help`
