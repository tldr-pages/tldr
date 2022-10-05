# nova

> The OpenStack project that provides a way to provision compute instances.
> More information: <https://docs.openstack.org/nova/latest/>.

- List VMs on current tenant:

`nova list`

- List VMs of all tenants (admin user only):

`nova list --all-tenants`

- Boot a VM on a specific host:

`nova boot --nic net-id={{net_id}} --image {{image_id}} --flavor {{flavor}} --availability-zone nova:{{host_name}} {{vm_name}}`

- Start a server:

`nova start {{server}}`

- Stop a server:

`nova stop {{server}}`

- Attach a network interface to a specific VM:

`nova interface-attach --net-id {{net_id}} {{server}}`
