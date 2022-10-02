# btrfs

> Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux.
> Alguns subcomandos como `btrfs device` têm sua própria documentação de uso.
> Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.
- Criar subvolume:

`sudo btrfs subvolume create {{caminho/para/subvolume}}`

- Liste subvolumes:

`sudo btrfs subvolume list {{caminho/para/ponto_de_montagem}}`

- Mostre informações de uso do espaço:

`sudo btrfs filesystem df {{caminho/para/ponto_de_montagem}}`

- Ative a cota:

`sudo btrfs quota enable {{caminho/para/subvolume}}`

- Mostre a cota:

`sudo btrfs qgroup show {{caminho/para/subvolume}}`
