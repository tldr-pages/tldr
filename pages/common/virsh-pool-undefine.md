# virsh pool-undefine

> Delete the configuration file in `/etc/libvirt/storage` for a stopped virtual machine storage pool.
> See also: `virsh`, `virsh-pool-destroy`.
> More information: <https://manned.org/virsh>.

- Delete the configuration for the storage pool specified name or UUID (determine using `virsh pool-list`):

`virsh pool-undefine --pool {{name|uuid}}`
