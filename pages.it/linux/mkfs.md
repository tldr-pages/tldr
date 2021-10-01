# mkfs

> Costruisce un filesystem Linux su una partizione del disco rigido.
> Questo comando è deprecato in favore degli strumenti specifici per filesystem: mkfs.tipo.
> Maggiori informazioni: <https://manned.org/mkfs>.

- Costruisce un filesystem Linux ext2 su una partizione:

`mkfs {{percorso/alla/partizione}}`

- Costruisce un filesystem del tipo specificato:

`mkfs -t {{ext4}} {{percorso/alla/partizione}}`

- Costruisce un filesystem del specificato e controlla la presenza di settori danneggiati:

`mkfs -c -t {{ntfs}} {{percorso/alla/partizione}}`
