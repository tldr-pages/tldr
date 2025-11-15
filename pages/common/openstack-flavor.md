# openstack flavor

> Manage OpenStack instance flavors (virtual hardware templates).
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/flavor.html>.

- List all flavors:

`openstack flavor list`

- Show details of a flavor:

`openstack flavor show {{flavor_id_or_name}}`

- Create a new flavor with 2 vCPUs, 4GB RAM, and 20GB disk:

`openstack flavor create {{flavor_name}} --vcpus 2 --ram 4096 --disk 20`

- Delete a flavor:

`openstack flavor delete {{flavor_id_or_name}}`

- Create a flavor with 10GB ephemeral disk and 512MB swap space:

`openstack flavor create {{flavor_name}} --vcpus 4 --ram 8192 --disk 40 --ephemeral 10 --swap 512`
