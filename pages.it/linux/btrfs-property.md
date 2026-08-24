# btrfs property

> Ottiene, imposta o elenca proprietà per oggetti BTRFS (file, directory, sottovolumi, filesystem o dispositivi).
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- Elenca le proprietà disponibili (e descrizioni) per l'oggetto btrfs dato:

`sudo btrfs {{[p|property]}} {{[l|list]}} {{percorso/all/oggetto_btrfs}}`

- Ottiene tutte le proprietà per l'oggetto btrfs dato:

`sudo btrfs {{[p|property]}} {{[g|get]}} {{percorso/all/oggetto_btrfs}}`

- Ottiene la proprietà `label` per il filesystem o dispositivo btrfs dato:

`sudo btrfs {{[p|property]}} {{[g|get]}} {{percorso/al/filesystem_btrfs}} label`

- Ottiene tutte le proprietà specifiche del tipo di oggetto per il filesystem o dispositivo btrfs dato:

`sudo btrfs {{[p|property]}} {{[g|get]}} -t {{subvol|filesystem|inode|device}} {{percorso/al/filesystem_btrfs}}`

- Imposta la proprietà `compression` per un inode btrfs dato (file o directory):

`sudo btrfs {{[p|property]}} {{[s|set]}} {{percorso/all/inode_btrfs}} compression {{zstd|zlib|lzo|none}}`
