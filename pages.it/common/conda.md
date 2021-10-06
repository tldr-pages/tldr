# conda

> Gestione pacchetti, dipendenze ed ambiente per qualsiasi linguaggio di programmazione.
> Alcuni comandi aggiuntivi, come `conda create`, hanno la propria documentazione.
> Maggiori informazioni: <https://github.com/conda/conda>.

- Crea un nuovo ambiente, installandovi alcuni pacchetti:

`conda create --name {{nome_ambiente}} {{python=2.7 matplotlib}}`

- Elenca tutti gli ambienti:

`conda info --envs`

- Attiva o disattiva un ambiente:

`conda {{activate|deactivate}} {{nome_ambiente}}`

- Elimina un ambiente rimuovendo anche tutti i pacchetti:

`conda remove --name {{nome_ambiente}} --all`

- Cerca un determinato pacchetto nei canali di conda:

`conda search {{package_name}}`

- Installa pacchetti nell'ambiente corrente:

`conda install {{python=3.4 numpy}}`

- Elenca i pacchetti attualmente installati nell'ambiente corrente:

`conda list`

- Elimina pacchetti inutilizzati e cache:

`conda clean --all`
