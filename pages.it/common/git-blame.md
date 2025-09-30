# git blame

> Mostra hash del commit ed ultimo autore per ogni riga di un file.
> Maggiori informazioni: <https://git-scm.com/docs/git-blame>.

- Stampa il contenuto di un file annotando ogni riga con l'hash del commit e il nome dell'autore:

`git blame {{file}}`

- Stampa il contenuto di un file annotando ogni riga con l'hash del commit e l'indirizzo email dell'autore:

`git blame {{[-e|--show-email]}} {{file}}`
