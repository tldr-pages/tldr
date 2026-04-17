# hcloud

> Manage Hetzner Cloud resources.
> More information: <https://github.com/hetznercloud/cli>.

- Log in to a Hetzner Cloud project:

`hcloud context create {{context_name}}`

- List all servers:

`hcloud server list`

- Create a server:

`hcloud server create --name {{name}} --type {{server_type}} --image {{image_name}}`

- List all available server types:

`hcloud server-type list`

- List all available images:

`hcloud image list`

- Delete a server:

`hcloud server delete {{server_name_or_id}}`

- Display help for a subcommand:

`hcloud {{server|context|network|image}} --help`
