# apptainer cache

> Gestisce la cache locale di Apptainer.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_cache.html>.

- Elenca tutte le immagini container memorizzate nella cache:

`apptainer cache list`

- Elenca le immagini container memorizzate nella cache con informazioni dettagliate:

`apptainer cache list {{[-v|--verbose]}}`

- Elenca solo un tipo specifico di cache:

`apptainer cache list {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Pulisce l'intera cache:

`apptainer cache clean`

- Pulisce solo un tipo specifico di cache:

`apptainer cache clean {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Pulisce le voci della cache più vecchie di un numero specifico di giorni:

`apptainer cache clean {{[-D|--days]}} {{giorni}}`

- Mostra un'anteprima di cosa verrebbe pulito senza rimuovere nulla:

`apptainer cache clean {{[-n|--dry-run]}}`

- Forza la pulizia senza conferma:

`apptainer cache clean {{[-f|--force]}}`
