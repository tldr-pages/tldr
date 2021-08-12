# git ls-tree

> Listați conținutul unui obiect arbore.
> Mai multe informaţii: <https://git-scm.com/docs/git-ls-tree>

- Listați conținutul arborelui pe o ramură:

`git ls-tree {{branch_name}}`

- Listează conținutul arborelui pe o comite, recurente în subarbori:

`git ls-tree -r {{commit_hash}}`

- Lista numai numele de fișiere ale arborelui pe o comite:

`git ls-tree --name-only {{commit_hash}}`
