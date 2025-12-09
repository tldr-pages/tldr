# btrfs inspect-internal

> Consulta informazioni interne di un filesystem btrfs.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- Stampa le informazioni del superblock:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{percorso/alla/partizione}}`

- Stampa le informazioni del superblock e tutte le sue copie:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{[-a|--all]}} {{percorso/alla/partizione}}`

- Stampa le informazioni di metadati del filesystem:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-t|dump-tree]}} {{percorso/alla/partizione}}`

- Stampa l'elenco dei file nell'inode `n`-esimo:

`sudo btrfs {{[i|inspect-internal]}} {{[i|inode-resolve]}} {{n}} {{percorso/al/mount_btrfs}}`

- Stampa l'elenco dei file a un dato indirizzo logico:

`sudo btrfs {{[i|inspect-internal]}} {{[lo|logical-resolve]}} {{logical_address}} {{percorso/al/mount_btrfs}}`

- Stampa le statistiche di root, extent, csum e alberi fs:

`sudo btrfs {{[i|inspect-internal]}} {{[t|tree-stats]}} {{percorso/alla/partizione}}`
