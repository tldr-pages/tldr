# conda

> Gestione pacchetti, dipendenze ed ambiente per qualsiasi linguaggio di programmazione.
> Alcuni comandi aggiuntivi, come `create`, hanno la propria documentazione.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- Crea un nuovo ambiente, installandovi alcuni pacchetti:

`conda create {{[-n|--name]}} {{nome_ambiente}} {{python=3.9 matplotlib}}`

- Elenca tutti gli ambienti:

`conda info {{[-e|--envs]}}`

- Attiva un ambiente:

`conda activate {{nome_ambiente}}`

- Disattiva un ambiente:

`conda deactivate`

- Elimina un ambiente rimuovendo anche tutti i pacchetti:

`conda remove {{[-n|--name]}} {{nome_ambiente}} --all`

- Installa pacchetti nell'ambiente corrente:

`conda install {{python=3.4 numpy}}`

- Elenca i pacchetti attualmente installati nell'ambiente corrente:

`conda list`

- Elimina pacchetti inutilizzati e cache:

`conda clean {{[-a|--all]}}`
