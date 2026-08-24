# btrfs balance

> Bilancia i gruppi di blocchi su un filesystem btrfs.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- Mostra lo stato di un'operazione di bilanciamento in esecuzione o sospesa:

`sudo btrfs {{[b|balance]}} status {{percorso/al/filesystem_btrfs}}`

- Bilancia tutti i gruppi di blocchi (lento; riscrive tutti i blocchi nel filesystem):

`sudo btrfs {{[b|balance]}} start {{percorso/al/filesystem_btrfs}}`

- Bilancia i gruppi di blocchi dati con meno del 15% di utilizzo, eseguendo l'operazione in background:

`sudo btrfs {{[b|balance]}} start {{[--bg|--background]}} -dusage={{15}} {{percorso/al/filesystem_btrfs}}`

- Bilancia un massimo di 10 chunk di metadati con meno del 20% di utilizzo e almeno 1 chunk su un dispositivo specifico `devid` (vedi `btrfs filesystem show`):

`sudo btrfs {{[b|balance]}} start -musage={{20}},limit={{10}},devid={{devid}} {{percorso/al/filesystem_btrfs}}`

- Converte i blocchi dati in raid6 e i metadati in raid1c3 (vedi mkfs.btrfs(8) per i profili):

`sudo btrfs {{[b|balance]}} start -dconvert={{raid6}} -mconvert={{raid1c3}} {{percorso/al/filesystem_btrfs}}`

- Converte i blocchi dati in raid1, saltando i chunk già convertiti (es. dopo un'operazione di conversione precedente cancellata):

`sudo btrfs {{[b|balance]}} start -dconvert={{raid1}},soft {{percorso/al/filesystem_btrfs}}`

- Annulla, sospende o riprende un'operazione di bilanciamento in esecuzione o sospesa:

`sudo btrfs {{[b|balance]}} {{cancel|pause|resume}} {{percorso/al/filesystem_btrfs}}`
