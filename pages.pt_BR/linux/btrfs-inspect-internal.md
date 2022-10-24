# btrfs inspect-internal

> Consulta informações internas de um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-inspect-internal>.

- Imprime informações de superblocos:

`sudo btrfs inspect-internal dump-super {{caminho/para/partição}}`

- Imprime as informações do superbloco e de todas as suas cópias:

`sudo btrfs inspect-internal dump-super --all {{caminho/para/partição}}`

- Imprime informações de metadados do sistema de arquivos:

`sudo btrfs inspect-internal dump-tree {{caminho/para/partição}}`

- Imprime lista de arquivos no `n`-ésimo inode:

`sudo btrfs inspect-internal inode-resolve {{n}} {{caminho/para/montagem_btrfs}}`

- Imprime a lista de arquivos em um determinado endereço lógico:

`sudo btrfs inspect-internal logical-resolve {{endereço_lógico}} {{caminho/para/montagem_btrfs}}`

- Imprime as estatísticas das árvores raiz, extensão, csum e fs:

`sudo btrfs inspect-internal tree-stats {{caminho/para/partição}}`
