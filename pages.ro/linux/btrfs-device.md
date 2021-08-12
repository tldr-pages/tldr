# btrfs device

> Gestionați dispozitivele într-un sistem de fișiere Btrfs.
> Mai multe informaţii: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-device>

- Adăugați unul sau mai multe dispozitive la un sistem de fișiere btrfs:

`sudo btrfs device add {{path/to/block_device1}} [{{path/to/block_device2}}] {{path/to/btrfs_filesystem}}`

- Eliminați un dispozitiv dintr-un sistem de fișiere Btrfs:

`sudo btrfs device remove {{path/to/device|device_id}} [{{...}}]`

- Afișarea statisticilor erorilor:

`sudo btrfs device stats {{path/to/btrfs_filesystem}}`

- Scanați toate discurile și informați nucleul tuturor sistemelor de fișiere btrfs detectate:

`sudo btrfs device scan --all-devices`

- Afișează statistici detaliate de alocare pe disc:

`sudo btrfs device usage {{path/to/btrfs_filesystem}}`
