# qm migrate

> Migrate virtual machine. Creates a new migration task.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Migrate a virtual machine:

`qm migrate {{vm_id}} {{target}}`

- Override the current I/O bandwidth limit (in KiB/s):

`qm migrate {{vm_id}} {{target}} --bwlimit {{10}}`

- Allow to migrate VMs which use local devices:

`qm migrate {{vm_id}} {{target}} --force {{true}}`

- Use online/live migration (only use if Virtual Machine is running):

`qm migrate {{vm_id}} {{target}} --online {{true}}`

- Enable live storage migration for local disk:

`qm migrate {{vm_id}} {{target}} --with-local-disks {{true}}`
