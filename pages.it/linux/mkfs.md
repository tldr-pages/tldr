# mkfs

> Costruisce un filesystem Linux su una partizione del disco rigido.
> Questo comando è deprecato in favore degli strumenti specifici per filesystem: mkfs.tipo.
> Maggiori informazioni: <https://manned.org/mkfs>.

- Costruisce un filesystem Linux ext2 su una partizione:

`sudo mkfs {{percorso/della/partizione}}`

- Costruisce un filesystem del tipo specificato:

`sudo mkfs {{[-t|--type]}} {{ext4}} {{percorso/della/partizione}}`

- Costruisce un filesystem del specificato e controlla la presenza di settori danneggiati:

`sudo mkfs -c {{[-t|--type]}} {{ntfs}} {{percorso/della/partizione}}`
