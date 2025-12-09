# git replace

> Crea, elenca, ed elimina riferimenti ad oggetti sostituiti.
> Maggiori informazioni: <https://git-scm.com/docs/git-replace>.

- Sostituisci un commit con un altro, senza modificare gli altri commit:

`git replace {{oggetto}} {{oggetto_sostitutivo}}`

- Cancella riferimenti esistenti ad un oggetto sostituito:

`git replace --delete {{oggetto}}`

- Modifica il contenuto di un oggetto in modo interattivo:

`git replace --edit {{oggetto}}`
