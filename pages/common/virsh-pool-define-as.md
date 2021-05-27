# virsh-pool-define-as

> Create a configuration file in `/etc/libvirt/storage` for a persistent virtual machine storage pool from the provided arguments.
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Create the configuration file for a storage pool called pool_name using `/var/vms` as the underlying storage system (use `virsh pool-build` to create the underlying storage system and use `virsh pool-start` to start the inactive pool):

`virsh pool-define-as --name {{pool_name}} --type {{dir}} --target {{/var/vms}}`
