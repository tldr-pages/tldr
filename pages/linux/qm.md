# qm

> QEMU/KVM Virtual Machine Manager.
> Some subcommands such as `list`, `start`, `stop`, `clone`, etc. have their own usage documentation.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- List all virtual machines:

`qm list`

- Using an ISO file uploaded on the local storage, create a virtual machine with a 4 GB SCSI disk on the `local-lvm` storage and an ID of 100:

`qm {{[cr|create]}} {{100}} --scsi0 {{local-lvm:4}} --net0 {{e1000}} --cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- Show the configuration of a virtual machine, specifying its ID:

`qm {{[co|config]}} {{100}}`

- Start a specific virtual machine:

`qm start {{100}}`

- Send a shutdown request, then wait until the virtual machine is stopped:

`qm {{[shu|shutdown]}} {{100}} && qm {{[w|wait]}} {{100}}`

- Destroy a virtual machine and remove all related resources:

`qm {{[des|destroy]}} {{100}} --purge`
