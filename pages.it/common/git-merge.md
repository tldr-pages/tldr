# git merge

> Esegui un'unione (merge) tra due rami Git.
> Maggiori informazioni: <https://git-scm.com/docs/git-merge>.

- Avvia un'unione con il tuo ramo corrente:

`git merge {{ramo_da_unire}}`

- Avvia un'unione e cambia il messaggio predefinito:

`git merge --edit {{ramo_da_unire}}`

- Avvia un'unione e committa l'operazione:

`git merge --no-ff {{ramo_da_unire}}`

- Interrompi un'unione in caso di conflitti:

`git merge --abort`
