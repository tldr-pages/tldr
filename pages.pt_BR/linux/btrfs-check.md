# btrfs check

> Verifica ou repara um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Verifica um sistema de arquivos btrfs:

`sudo btrfs {{[c|check]}} {{caminho/para/partição}}`

- Verifica e repara um sistema de arquivos btrfs (perigoso):

`sudo btrfs {{[c|check]}} --repair {{caminho/para/partição}}`

- Mostra o andamento da verificação:

`sudo btrfs {{[c|check]}} {{[-p|--progress]}} {{caminho/para/partição}}`

- Verifica a soma de verificação de cada bloco de dados (se o sistema de arquivos estiver bom):

`sudo btrfs {{[c|check]}} --check-data-csum {{caminho/para/partição}}`

- Usa o `n`-ésimo superbloco (`n` pode ser 0, 1 ou 2):

`sudo btrfs {{[c|check]}} {{[-s|--super]}} {{n}} {{caminho/para/partição}}`

- Reconstrói a árvore de soma de verificação:

`sudo btrfs {{[c|check]}} --repair --init-csum-tree {{caminho/para/partição}}`

- Reconstrói a árvore de extensão:

`sudo btrfs {{[c|check]}} --repair --init-extent-tree {{caminho/para/partição}}`
