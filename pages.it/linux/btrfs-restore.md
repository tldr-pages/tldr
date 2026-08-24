# btrfs restore

> Tenta di recuperare i file da un filesystem btrfs danneggiato.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Ripristina tutti i file da un filesystem btrfs in una directory specificata:

`sudo btrfs {{[rest|restore]}} {{percorso/al/device/btrfs}} {{percorso/alla/directory_target}}`

- Elenca (non scrive) i file da ripristinare da un filesystem btrfs:

`sudo btrfs {{[rest|restore]}} {{[-D|--dry-run]}} {{percorso/al/device/btrfs}} {{percorso/alla/directory_target}}`

- Ripristina file che corrispondono a un dato `regex` ([c]ase-insensitive) da un filesystem btrfs (tutte le directory genitore dei file target devono corrispondere):

`sudo btrfs {{[rest|restore]}} --path-regex {{regex}} -c {{percorso/al/device/btrfs}} {{percorso/alla/directory_target}}`

- Ripristina file da un filesystem btrfs usando un albero root specifico [t]ree `bytenr` (vedi `btrfs-find-root`):

`sudo btrfs {{[rest|restore]}} -t {{bytenr}} {{percorso/al/device/btrfs}} {{percorso/alla/directory_target}}`

- Ripristina file da un filesystem btrfs (insieme a metadati, attributi estesi e Symlink), sovrascrivendo i file nel target:

`sudo btrfs {{[rest|restore]}} {{[-m|--metadata]}} {{[-x|--xattr]}} {{[-S|--symlinks]}} {{[-o|--overwrite]}} {{percorso/al/device/btrfs}} {{percorso/alla/directory_target}}`
