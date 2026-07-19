# qm

> QEMU/KVM Virtual Machine Manager.
> Some subcommands such as `list`, `start`, `stop`, `clone`, etc. have their own usage documentation.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- List all virtual machines:

`qm list`

- Create a virtual machine with a 4 GB SCSI disk on the `local-lvm` storage and a specific ID using an ISO file uploaded on the `local` storage:

`qm {{[cr|create]}} {{vm_id}} --scsi0 local-lvm:4 --net0 {{e1000}} --cdrom local:{{iso/proxmox-mailgateway_2.1.iso}}`

- Show the configuration of a virtual machine, specifying its ID:

`qm {{[co|config]}} {{vm_id}}`

- Start a specific virtual machine:

`qm start {{vm_id}}`

- Send a shutdown request, then wait until the virtual machine is stopped:

`qm {{[shu|shutdown]}} {{vm_id}} && qm {{[w|wait]}} {{vm_id}}`

- Destroy a virtual machine and remove all related resources:

`qm {{[des|destroy]}} {{vm_id}} --purge`
