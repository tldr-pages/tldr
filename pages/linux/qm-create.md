# qm create

> Create or restore a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Create a virtual machine with access to 512MiB of memory and 1 CPU core:

`qm {{[cr|create]}} {{100}}`

- Automatically start the machine after creation:

`qm {{[cr|create]}} {{100}} --start`

- Give the virtual machine a name:

`qm {{[cr|create]}} {{100}} --name {{vm_name}}`

- Specify the type of operating system on the machine:

`qm {{[cr|create]}} {{100}} --ostype {{win10}}`

- Replace an existing machine (requires archiving it):

`qm {{[cr|create]}} {{100}} --archive {{path/to/backup_file.tar}} --force 1`

- Specify a script that is executed automatically depending on the state of the virtual machine:

`qm {{[cr|create]}} {{100}} --hookscript {{path/to/script.pl}}`

- Specify the install media:

`qm {{[cr|create]}} {{100}} --cdrom {{local:iso/install-media.iso}}`

- Create a VM that bridges itself to the host network:

`qm {{[cr|create]}} {{100}} --net{{0}} virtio,bridge=vmbr{{0}}`
