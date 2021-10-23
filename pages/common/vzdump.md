# vzdump

> Backup Utility for VMs and Containers.
> More information: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- Dump guest VM into default dump directory (usually /var/lib/vz/dump/), no snapshot:

`vzdump {{VM_ID}}`

- Backup guest 101, 102, and 103:

`vzdump {{101 102 103}}`

- Dump guest VM using specific mode:

`vzdump {{VM_ID}} --mode {{suspend|snapshot}}`

- Backup all guest systems and send notification mails to root and admin:

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- Use snapshot mode (no downtime) and non-default dump directory:

`vzdump {{VM_ID}} --dumpdir /mnt/backup --mode snapshot`

- Backup all guests excluding 101 and 102:

`vzdump --mode {{suspend}} --exclude {{101, 102}}`
