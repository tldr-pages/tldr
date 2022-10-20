# poetry

> Gestore di pacchetti e dipendenze per Python.
> Maggiori informazioni: <https://python-poetry.org/docs/cli/>.

- Crea un nuovo progetto Poetry nella cartella specificata:

`poetry new {{nome_progetto}}`

- Installa una dipendenza e le relative sottodipendenze:

`poetry add {{dipendenza}}`

- Inizializza interattivamente la nuova cartella come un nuovo progetto Poetry:

`poetry init`

- Recupera l'ultima versione di ciascuna dipendenza e aggiorna il file `poetry.lock`:

`poetry update`

- Esegue un comando all'interno dell'ambiente virtuale del progetto:

`poetry run {{comando}}`
