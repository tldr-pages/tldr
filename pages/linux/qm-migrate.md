# qm migrate

> Migrate a virtual machine.
> Used to create a new migration task.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_migrate>.

- Migrate a specific virtual machine:

`qm {{[mi|migrate]}} {{100}} {{target}}`

- Override the current I/O bandwidth limit with 10 KiB/s:

`qm {{[mi|migrate]}} {{100}} {{target}} --bwlimit 10`

- Allow migration of virtual machines using local devices (root only):

`qm {{[mi|migrate]}} {{100}} {{target}} --force true`

- Use online/live migration if a virtual machine is running:

`qm {{[mi|migrate]}} {{100}} {{target}} --online true`

- Enable live storage migration for local disks:

`qm {{[mi|migrate]}} {{100}} {{target}} --with-local-disks true`
