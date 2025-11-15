# openstack network

> Manage OpenStack network resources.
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/network.html>.

- List all networks:

`openstack network list`

- Show details of a network:

`openstack network show {{network_id_or_name}}`

- Create a new network with a given name:

`openstack network create {{network_name}}`

- Delete a network:

`openstack network delete {{network_id_or_name}}`

- Enable a network:

`openstack network set --enable {{network_id_or_name}}`

- Disable a network:

`openstack network set --disable {{network_id_or_name}}`
