# git ls-tree

> Egy faobjektum tartalmának listázása. További információ: <https://git-scm.com/docs/git-ls-tree>.

- A fa tartalmának listázása egy ágon:

`git ls-tree {{branch_name}}`

- A fa tartalmának listázása egy commiton, rekurzívan a részfákba:

`git ls-tree -r {{commit_hash}}`

- Csak a fa fájlneveinek listázása egy commiton:

`git ls-tree --name-only {{commit_hash}}`
