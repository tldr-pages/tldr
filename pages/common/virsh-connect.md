# virsh-connect

> Connect to a virtual machine hypervisor.
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- Connect to the default hypervisor:

`virsh connect`

- Connect as root to the local QEMU/KVM hypervisor:

`virsh connect qemu:///system`

- Launch a new instance of the hypervisor and connect to it as the local user:

`virsh connect qemu:///session`

- Connect as root to a remote hypervisor using ssh:

`virsh connect qemu+ssh://{{user_name@host_name}}/system`
