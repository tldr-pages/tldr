# btrfs

> Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux.
> Alguns subcomandos como `btrfs device` têm sua própria documentação de uso.
> Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Criar subvolume:

`sudo btrfs subvolume create {{caminho/para/subvolume}}`

- Listar subvolumes:

`sudo btrfs subvolume list {{caminho/para/ponto_de_montagem}}`

- Mostrar informações de uso do espaço:

`sudo btrfs filesystem df {{caminho/para/ponto_de_montagem}}`

- Ativar cota:

`sudo btrfs quota enable {{caminho/para/subvolume}}`

- Mostrar cota:

`sudo btrfs qgroup show {{caminho/para/subvolume}}`
