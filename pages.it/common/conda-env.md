# conda env

> Gestisce gli ambienti conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>.

- Crea un ambiente da un file di ambiente (YAML, TXT, ecc.):

`conda env create {{[-f|--file]}} {{percorso/al/file}}`

- Elimina un ambiente e tutto il suo contenuto:

`conda env remove {{[-n|--name]}} {{nome_ambiente}}`

- Aggiorna un ambiente basandosi su un file di ambiente:

`conda env update {{[-f|--file]}} {{percorso/al/file}} --prune`

- Elenca tutti gli ambienti:

`conda env list`

- Visualizza i dettagli dell'ambiente:

`conda env export`

- Elenca le variabili d'ambiente:

`conda env config vars list`

- Imposta variabili d'ambiente:

`conda env config vars set {{mia_var}}={{valore}}`
