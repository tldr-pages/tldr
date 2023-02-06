# btrfs inspect-internal

> A btrfs fájlrendszer belső információinak lekérdezése. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- A szuperblokk információinak nyomtatása:

`sudo btrfs inspect-internal dump-super {{path/to/partition}}`

- A szuperblokk és annak összes másolatának információinak nyomtatása:

`sudo btrfs inspect-internal dump-super --all {{path/to/partition}}`

- A fájlrendszer metaadatainak nyomtatása:

`sudo btrfs inspect-internal dump-tree {{path/to/partition}}`

- A fájlok listájának nyomtatása az inode-ban `n`-th:

`sudo btrfs inspect-internal inode-resolve {{n}} {{path/to/btrfs_mount}}`

- Az adott logikai címen lévő fájlok listájának nyomtatása:

`sudo btrfs inspect-internal logical-resolve {{logical_address}} {{path/to/btrfs_mount}}`

- A root, extent, csum és fs fák statisztikáinak nyomtatása:

`sudo btrfs inspect-internal tree-stats {{path/to/partition}}`
