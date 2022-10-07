# qm create

> Erzeugung einer virtuellen Maschine per QEMU/KVM Virtual Machine Manager.
> Weitere Informationen: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Erzeuge eine virtuelle Maschine:

`qm create {{100}}`

- Erzeuge eine virtuelle Maschine und starte sie unmittelbar danach im Anschluss:

`qm create {{100}} --start 1`

- Lege den Typ des Betriebssystems auf der virtuellen Maschine fest:

`qm create {{100}} --ostype {{win10}}`

- Ersetze eine bestehende virtuelle Maschine (setzt deren Archivierung voraus):

`qm create {{100}} --archive {{pfad/zu/backup_file.tar}} --force 1`

- Lege ein Skript fest, welches automatisch abhängig vom Zustand der virtuellen Maschine ausgelöst werden soll:

`qm create {{100}} --hookscript {{pfad/zu/script.pl}}`
