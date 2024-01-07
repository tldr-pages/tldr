# conda

> Gestione pacchetti, dipendenze ed ambiente per qualsiasi linguaggio di programmazione.
> Alcuni comandi aggiuntivi, come `conda create`, hanno la propria documentazione.
> Maggiori informazioni: <https://github.com/conda/conda>.

- Crea un nuovo ambiente, installandovi alcuni pacchetti:

`conda create --name {{nome_ambiente}} {{python=3.9 matplotlib}}`

- Elenca tutti gli ambienti:

`conda info --envs`

- Attiva un ambiente:

`conda activate {{nome_ambiente}}`

- Disattiva un ambiente:

`conda deactivate`

- Elimina un ambiente rimuovendo anche tutti i pacchetti:

`conda remove --name {{nome_ambiente}} --all`

- Installa pacchetti nell'ambiente corrente:

`conda install {{python=3.4 numpy}}`

- Elenca i pacchetti attualmente installati nell'ambiente corrente:

`conda list`

- Elimina pacchetti inutilizzati e cache:

`conda clean --all`
