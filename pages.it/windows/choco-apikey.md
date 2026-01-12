# choco apikey

> Gestisci le chiavi API per le fonti di Chocolatey.
> Maggiori informazioni: <https://docs.chocolatey.org/en-us/create/commands/api-key/>.

- Mostra una lista di fonti e le loro chiavi API:

`choco apikey`

- Mostra una specifica fonte e la sua chiave API:

`choco apikey {{[-s|--source]}} "{{url_della_fonte}}"`

- Imposta una chiave API per una fonte:

`choco apikey {{[-s|--source]}} "{{url_della_fonte}}" {{[-k|--api-key]}} "{{chiave_api}}"`

- Rimuovi una chiave API per una fonte:

`choco apikey {{[-s|--source]}} "{{url_della_fonte}}" --remove`
