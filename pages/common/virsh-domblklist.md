# virsh-domblklist

> List information about block devices associated with a virtual machine.
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- List the target name and source path of the block devices:

`virsh domblklist --domain {{vm_name}}`

- List the disk type and device value as well as the target name and source path:

`virsh domblklist --domain {{vm_name}} --details`
