# git cat-file

> Visualizza il contenuto di un oggetto git nel repository o mostrane dimensione e tipo.
> Maggiori informazioni: <https://git-scm.com/docs/git-cat-file>.

- Mostra la dimen[s]ione del commit HEAD in byte:

`git cat-file -s HEAD`

- Mostra il [t]ipo (blob, albero, commit, tag) di un oggetto git:

`git cat-file -t {{8c442dc3}}`

- Stam[p]a il contenuto di un oggetto git, formattato in base al tipo:

`git cat-file -p {{HEAD~2}}`
