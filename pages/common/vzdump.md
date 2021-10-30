# vzdump

> Backup Utility for virtual machines and containers.
> More information: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- Dump a guest virtual machine into default dump directory (usually `/var/lib/vz/dump/`), no snapshot:

`vzdump {{vm_id}}`

- Backup guest 101, 102, and 103:

`vzdump {{101 102 103}}`

- Dump a guest virtual machine using specific mode:

`vzdump {{vm_id}} --mode {{suspend|snapshot}}`

- Backup all guest systems and send notification mails to root and admin:

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- Use snapshot mode (no downtime) and non-default dump directory:

`vzdump {{vm_id}} --dumpdir {{path/to/directory}} --mode snapshot`

- Backup all guests excluding 101 and 102:

`vzdump --mode {{suspend}} --exclude {{101, 102}}`
