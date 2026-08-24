# btrfs inspect-internal

> Consulta informações internas de um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- Imprime informações de superblocos:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{caminho/para/partição}}`

- Imprime as informações do superbloco e de todas as suas cópias:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{[-a|--all]}} {{caminho/para/partição}}`

- Imprime informações de metadados do sistema de arquivos:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-t|dump-tree]}} {{caminho/para/partição}}`

- Imprime lista de arquivos no `n`-ésimo inode:

`sudo btrfs {{[i|inspect-internal]}} {{[i|inode-resolve]}} {{n}} {{caminho/para/montagem_btrfs}}`

- Imprime a lista de arquivos em um determinado endereço lógico:

`sudo btrfs {{[i|inspect-internal]}} {{[lo|logical-resolve]}} {{endereço_lógico}} {{caminho/para/montagem_btrfs}}`

- Imprime as estatísticas das árvores raiz, extensão, csum e fs:

`sudo btrfs {{[i|inspect-internal]}} {{[t|tree-stats]}} {{caminho/para/partição}}`
