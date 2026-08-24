# btrfs check

> Controlla o ripara un filesystem btrfs.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Controlla un filesystem btrfs:

`sudo btrfs {{[c|check]}} {{percorso/alla/partizione}}`

- Controlla e ripara un filesystem btrfs (pericoloso):

`sudo btrfs {{[c|check]}} --repair {{percorso/alla/partizione}}`

- Mostra il progresso del controllo:

`sudo btrfs {{[c|check]}} {{[-p|--progress]}} {{percorso/alla/partizione}}`

- Verifica il checksum di ogni blocco dati (se il filesystem è integro):

`sudo btrfs {{[c|check]}} --check-data-csum {{percorso/alla/partizione}}`

- Usa il `n`-esimo superblock (`n` può essere 0, 1 o 2):

`sudo btrfs {{[c|check]}} {{[-s|--super]}} {{n}} {{percorso/alla/partizione}}`

- Ricostruisce l'albero dei checksum:

`sudo btrfs {{[c|check]}} --repair --init-csum-tree {{percorso/alla/partizione}}`

- Ricostruisce l'albero degli extent:

`sudo btrfs {{[c|check]}} --repair --init-extent-tree {{percorso/alla/partizione}}`
