# openstack subnet

> Manage OpenStack subnets (IP address blocks within a network).
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/subnet.html>.

- List all subnets:

`openstack subnet list`

- Show details of a specific subnet:

`openstack subnet show {{subnet_id_or_name}}`

- List subnets associated with a network:

`openstack subnet list --network {{network_id_or_name}}`

- Create a subnet with subnet range `192.168.0.0/24` in a given network:

`openstack subnet create --network {{network_id_or_name}} --subnet-range 192.168.0.0/24 {{subnet_name}}`

- Delete a subnet:

`openstack subnet delete {{subnet_id_or_name}}`

- Update a subnet with DNS `8.8.8.8` and set a new name:

`openstack subnet set --dns-nameserver 8.8.8.8 --name {{new_subnet_name}} {{subnet_id}}`
