# atoum

> Un semplice, moderno ed intuitivo framework PHP per unit testing.
> Maggiori informazioni: <https://atoum.readthedocs.io/en/latest/option_cli.html>.

- Inizializza un file di configurazione:

`atoum --init`

- Esegui tutti i test:

`atoum`

- Esegui test utilizzando uno specifico file di configurazione:

`atoum {{[-c|--configuration]}} {{percorso/del/file}}`

- Esegui uno specifico file di test:

`atoum {{[-f|--files]}} {{percorso/del/file}}`

- Esegui una specifica directory di test:

`atoum {{[-d|--directories]}} {{percorso/della/directory}}`

- Esegui tutti i test sotto uno specifico namespace:

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- Esegui tutti i test con uno specifico tag:

`atoum {{[-t|--tags]}} {{tag}}`

- Carica un file di bootstrap personalizzato prima di eseguire i test:

`atoum {{[-bf|--bootstrap-file]}} {{percorso/del/file}}`
