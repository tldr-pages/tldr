# qmrestore

> Restore QemuServer vzdump Backups.
> More information: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restore KVM-based virtual machine to local storage:

`qmrestore {{/var/lib/vz/dump/backup_file.vma.lzo}} {{vm_id}} --storage {{local}}`
