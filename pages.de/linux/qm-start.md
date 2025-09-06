# qm start

> Starte eine virtuelle Maschine per QEMU/KVM Virtual Machine Manager.
> Weitere Informationen: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Starte eine bestimmte virtuelle Maschine:

`qm start {{100}}`

- Lege den QEMU Maschinentyp fest (etwa den zu emulierenden Prozessor):

`qm start {{100}} --machine {{q35}}`

- Starte eine bestimmte virtuelle Maschine mit einem Timeout (Zeitabschaltung) nach 60 Sekunden:

`qm start {{100}} --timeout {{60}}`
