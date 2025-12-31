# git shortlog

> Riassume l'output di `git log`.
> Maggiori informazioni: <https://git-scm.com/docs/git-shortlog>.

- Mostra un riassunto dei commit fatti, raggruppati alfabeticamente per nome dell'autore:

`git shortlog`

- Mostra un riassunto dei commit fatti, ordinati per numero di commit:

`git shortlog {{[-n|--numbered]}}`

- Mostra un riassunto dei commit fatti, raggruppati per identità dell'utente che ha eseguito il commit (nome e email):

`git shortlog {{[-c|--committer]}}`

- Mostra un riassunto degli ultimi 5 commit (richiesti sottoforma di intervallo di revisione):

`git shortlog HEAD~5..HEAD`

- Mostra tutti gli utenti, email e numero di commit nel ramo corrente:

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}}`

- Mostra tutti gli utenti, email e numero di commit in tutti i rami:

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}} --all`
