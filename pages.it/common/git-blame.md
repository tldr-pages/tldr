# git blame

> Annota le righe di un file col loro codice di revisione (commit hash) e con l'autore che le ha modificate per ultimo.
> Maggiori informazioni: <https://git-scm.com/docs/git-blame>.

- Stampa il contenuto di un file su standard output, precedendo ogni riga con il suo commit hash e con il nome dell'autore:

`git blame {{file}}`

- Stampa il contenuto di un file precedendo ogni riga con il suo commit hash e con l'indirizzo email dell'autore:

`git blame -e {{file}}`
