# virsh-pool-delete

> Delete the underlying storage system of an inactive virtual machine storage pool (stop a storage pool with `virsh pool-destroy` and delete the storage pool configuration file with `virsh pool-undefine`).
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Delete the underlying storage system for the storage pool specified by name or UUID (determine the name or UUID using `virsh pool-list`):

`virsh pool-delete --pool {{name|uuid}}`
