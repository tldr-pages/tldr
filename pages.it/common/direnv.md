# direnv

> Estensione della shell per aggiungere o rimuovere variabili d'ambiente in base alla directory corrente.
> Maggiori informazioni: <https://github.com/direnv/direnv>.

- Permette il caricamento del `.envrc` presente nella directory corrente:

`direnv allow {{.}}`

- Revoca il permesso del `.envrc` presente nella directory corrente:

`direnv deny {{.}}`

- Permette la modifica del `.envrc` nell'editor di testo predefinito, in seguito ricarica l'ambiente:

`direnv edit {{.}}`

- Ricarica l'ambiente corrente:

`direnv reload`

- Mostra delle informazioni di debug:

`direnv status`
