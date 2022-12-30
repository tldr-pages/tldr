# btrfs

> Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux.
> Alguns subcomandos como `btrfs device` têm sua própria documentação de uso.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Cria subvolume:

`sudo btrfs subvolume create {{caminho/para/subvolume}}`

- Lista subvolumes:

`sudo btrfs subvolume list {{caminho/para/ponto_de_montagem}}`

- Mostra informações de uso do espaço:

`sudo btrfs filesystem df {{caminho/para/ponto_de_montagem}}`

- Ativa a cota:

`sudo btrfs quota enable {{caminho/para/subvolume}}`

- Mostra a cota:

`sudo btrfs qgroup show {{caminho/para/subvolume}}`
