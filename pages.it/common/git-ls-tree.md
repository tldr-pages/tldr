# git ls-tree

> Elenca il contenuto di un oggetto albero.
> Maggiori informazioni: <https://git-scm.com/docs/git-ls-tree>.

- Mostra il contenuto dell'albero su un ramo:

`git ls-tree {{nome_ramo}}`

- Mostra il contenuto dell'albero su un commit, procedendo ricorsivamente nei sotto-alberi:

`git ls-tree -r {{hash_commit}}`

- Mostra solo il nome dei file dell'albero su un commit:

`git ls-tree --name-only {{hash_commit}}`
