# apptainer run-help

> Mostra la guida definita dall'utente per un'immagine container Apptainer.
> Il testo della guida è definito nella sezione `%help` del file di definizione del container.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_run-help.html>.

- Mostra la guida per un container:

`apptainer run-help {{path/to/immagine.sif}}`

- Mostra la guida per un'app specifica all'interno di un container:

`apptainer run-help --app {{nome_app}} {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer run-help {{[-h|--help]}}`
