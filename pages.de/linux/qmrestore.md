# qmrestore

> Wiederherstellung von QemuServer vzdump Backups.
> Weitere Informationen: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Wiederherstellung einer virtuellen Maschine mittels Backupdatei auf dem ursprünglichen Speicher:

`qmrestore {{pfad/zu/vzdump-qemu-100.vma.lzo}} {{100}}`

- Überschreibung einer bestehenden virtuellen Maschine auf dem ursprünglichen Speicher:

`qmrestore {{pfad/zu/vzdump-qemu-100.vma.lzo}} {{100}} --force true`

- Wiederherstellung einer virtuellen Maschine auf einem bestimmten Speicher:

`qmrestore {{pfad/zu/vzdump-qemu-100.vma.lzo}} {{100}} --storage {{local}}`

- Sofortiger Start einer virtuellen Maschine bei gleichzeitiger Wiederherstellung im Hintergrund (nur bei Proxmox Backup Server):

`qmrestore {{pfad/zu/vzdump-qemu-100.vma.lzo}} {{100}} --live-restore true`
