# virsh pool-build

> Build the underlying storage system for a virtual machine storage pool as defined in it's configuration file in `/etc/libvirt/storage`.
> See also: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
> More information: <https://manned.org/virsh>.

- Build the storage pool specified by name or UUID (determine using `virsh pool-list`):

`virsh pool-build --pool {{name|uuid}}`
