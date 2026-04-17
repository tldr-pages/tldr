# openstack

> Manage OpenStack cloud resources.
> Some subcommands such as `server`, `network`, `image`, `volume`, and `flavor` have their own usage documentation.
> More information: <https://docs.openstack.org/python-openstackclient/latest/>.

- List all running servers:

`openstack server list`

- Create a new server:

`openstack server create --image {{image_id}} --flavor {{flavor_id}} --network {{network_id}} {{server_name}}`

- List all available images:

`openstack image list`

- List all networks:

`openstack network list`

- List all volumes:

`openstack volume list`

- List all available flavors:

`openstack flavor list`

- Display help for a subcommand:

`openstack {{server|network|image|volume|flavor}} --help`
