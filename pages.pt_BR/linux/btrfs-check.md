# btrfs check

> Verifica ou repara um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Verifica um sistema de arquivos btrfs:

`sudo btrfs check {{caminho/para/partição}}`

- Verifica e repara um sistema de arquivos btrfs (perigoso):

`sudo btrfs check --repair {{caminho/para/partição}}`

- Mostra o andamento da verificação:

`sudo btrfs check --progress {{caminho/para/partição}}`

- Verifica a soma de verificação de cada bloco de dados (se o sistema de arquivos estiver bom):

`sudo btrfs check --check-data-csum {{caminho/para/partição}}`

- Usa o `n`-ésimo superbloco (`n` pode ser 0, 1 ou 2):

`sudo btrfs check --super {{n}} {{caminho/para/partição}}`

- Reconstrói a árvore de soma de verificação:

`sudo btrfs check --repair --init-csum-tree {{caminho/para/partição}}`

- Reconstrói a árvore de extensão:

`sudo btrfs check --repair --init-extent-tree {{caminho/para/partição}}`
