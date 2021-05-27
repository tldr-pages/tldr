# virsh-pool-destroy

> Stop an active virtual machine storage pool (delete a stopped storage pool using `virsh pool-delete`).
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Stop a storage pool specified by name or UUID (determine the name or UUID using `virsh pool-list`):

`virsh pool-destroy --pool {{name|uuid}}`
