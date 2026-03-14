# conda env

> Gestisci ambienti conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>.

- Crea ambiente da file:

`conda env create {{[-f|--file]}} {{percorso/del/file}}`

- Elimina ambiente:

`conda env remove {{[-n|--name]}} {{nome_ambiente}}`

- Aggiorna ambiente da file:

`conda env update {{[-f|--file]}} {{percorso/del/file}} --prune`

- Elenca ambienti:

`conda env list`

- Dettagli ambiente:

`conda env export`

- Variabili ambiente:

`conda env config vars list`

- Imposta variabili:

`conda env config vars set {{VAR}}={{valore}}`
