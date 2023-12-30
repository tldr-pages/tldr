# git stash

> Salva in un'area temporanea (stash) modifiche Git locali.
> Maggiori informazioni: <https://git-scm.com/docs/git-stash>.

- Salva in un'area temporanea modifiche locali, tranne i file nuovi e non tracciati:

`git stash push -m {{messaggio_di_stash_opzionale}}`

- Includi nello stash anche i file nuovi e non tracciati:

`git stash -u`

- Seleziona per lo stash parti di file modificati in modo interattivo:

`git stash -p`

- Elenca tutti gli stash, mostrandone il nome, ramo relativo e messaggio:

`git stash list`

- Applica uno stash (quello predefinito è l'ultimo, chiamato stash@{0}):

`git stash apply {{nome_o_commit_stash_opzionale}}`

- Applica uno stash (il predefinito è stash@{0}) e rimuovilo dalla lista degli stash se non ha causato conflitti:

`git stash pop {{nome_stash_opzionale}}`

- Rimuovi tutti gli stash:

`git stash clear`
