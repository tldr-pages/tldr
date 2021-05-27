# virsh-pool-build

> Build the underlying storage system for a virtual machine storage pool as defined in it's configuration file (create a configuration file using `virsh pool-define-as`).
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Build the storage pool specified by name or UUID (determine the name or UUID using `virsh pool-list` and start the pool once built using `virsh pool-start`):

`virsh pool-build --pool {{name|uuid}}`
