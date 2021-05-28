# virsh pool-start

> Start a previously configured but inactive virtual machine storage pool (configure a pool with `virsh pool-define-as` and stop a pool with `virsh pool-destroy`).
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Start the storage pool specified by name or UUID (determine using `virsh pool-list`) and create the underlying storage system if it doesn't exist:

`virsh pool-start --pool {{name|uuid}} --build`
