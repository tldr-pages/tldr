# choco apikey

> Gestisci le chiavi API per le fonti di Chocolatey.
> Maggiori informazioni: <https://chocolatey.org/docs/commands-apikey>.

- Mostra una lista di fonti e le loro chiavi API:

`choco apikey`

- Mostra una specifica fonte e la sua chiave API:

`choco apikey --source "{{url_della_fonte}}"`

- Imposta una chiave API per una fonte:

`choco apikey --source "{{url_della_fonte}}" --key "{{chiave_api}}"`

- Rimuovi una chiave API per una fonte:

`choco apikey --source "{{url_della_fonte}}" --remove`
