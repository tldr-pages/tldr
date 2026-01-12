# btrfs

> Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux.
> Alguns subcomandos como `device` têm sua própria documentação de uso.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Cria subvolume:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{caminho/para/subvolume}}`

- Lista subvolumes:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{caminho/para/ponto_de_montagem}}`

- Mostra informações de uso do espaço:

`sudo btrfs {{[f|filesystem]}} df {{caminho/para/ponto_de_montagem}}`

- Ativa a cota:

`sudo btrfs {{[qu|quota]}} {{[e|enable]}} {{caminho/para/subvolume}}`

- Mostra a cota:

`sudo btrfs {{[qg|qgroup]}} {{[s|show]}} {{caminho/para/subvolume}}`
