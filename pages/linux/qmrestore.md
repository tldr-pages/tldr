# qmrestore

> Restore QemuServer `vzdump` backups.
> More information: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restore virtual machine from given backup file on the original storage:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{vm_id}}`

- Overwrite existing virtual machine from a given backup file on the original storage:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{vm_id}} --force true`

- Restore the virtual machine from a given backup file on specific storage:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{vm_id}} --storage {{local}}`

- Start virtual machine immediately from the backup while restoring in the background (only on Proxmox Backup Server):

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{vm_id}} --live-restore true`
