# qm create

> Create or restore a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Create a virtual machine:

`qm create {{100}}`

- Automatically start the machine after creation:

`qm create {{100}} --start 1`

- Specify the type of operating system on the machine:

`qm create {{100}} --ostype {{win10}}`

- Replace an existing machine (requires archiving it):

`qm create {{100}} --archive {{path/to/backup_file.tar}} --force 1`

- Specify a script that is executed on specific triggers during machine lifetime:

`qm create {{100}} --hookscript {{path/to/script.pl}}`
