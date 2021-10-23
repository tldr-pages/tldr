# qmrestore

> Restore QemuServer vzdump Backups.
> More information: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Restore KVM-based VM to local storage:

`qmrestore {{/var/lib/vz/dump/backup_file.vma.lzo}} {{VM_ID}} --storage local`
