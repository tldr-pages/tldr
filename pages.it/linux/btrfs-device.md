# btrfs device

> Gestisce i dispositivi in un filesystem btrfs.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Aggiunge uno o più dispositivi a un filesystem btrfs:

`sudo btrfs {{[d|device]}} {{[a|add]}} {{percorso/al/block_device1 percorso/al/block_device2 ...}} {{percorso/al/filesystem_btrfs}}`

- Rimuove un dispositivo da un filesystem btrfs:

`sudo btrfs {{[d|device]}} {{[rem|remove]}} {{percorso/al/device1|device_id1 percorso/al/device2|device_id2 ...}}`

- Mostra le statistiche degli errori:

`sudo btrfs {{[d|device]}} {{[st|stats]}} {{percorso/al/filesystem_btrfs}}`

- Scansiona tutti i dischi e informa il kernel di tutti i filesystem btrfs rilevati:

`sudo btrfs {{[d|device]}} {{[sc|scan]}} {{[-d|--all-devices]}}`

- Mostra statistiche dettagliate di allocazione per disco:

`sudo btrfs {{[d|device]}} {{[u|usage]}} {{percorso/al/filesystem_btrfs}}`
