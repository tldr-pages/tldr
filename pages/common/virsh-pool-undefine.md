# virsh pool-undefine

> Delete the configuration file in `/etc/libvirt/storage` for a stopped virtual machine storage pool (stop a pool using `virsh pool-destroy`).
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Delete the configuration for the storage pool specified name or UUID (determine the name or UUID using `virsh pool-list`):

`virsh pool-undefine --pool {{name|uuid}}`
