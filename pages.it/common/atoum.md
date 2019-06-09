# atoum

> Un semplice, moderno ed intuitivo framework PHP per unit testing.
> Maggiori informazioni: <http://atoum.org>.

- Inizializza un file di configurazione:

`atoum --init`

- Esegui tutti i test:

`atoum`

- Esegui test utilizzando uno specifico file di configurazione:

`atoum -c {{percorso/al/file}}`

- Esegui uno specifico file di test:

`atoum -f {{percorso/al/file}}`

- Esegui una specifica directory di test:

`atoum -d {{path/to/directory}}`

- Esegui tutti i test sotto uno specifico namespace:

`atoum -ns {{namespace}}`

- Esegui tutti i test con uno speficico tag:

`atoum -t {{tag}}`

- Carica un file di bootstrap personalizzato prima di eseguire i test:

`atoum --bootstrap-file {{percorso/al/file}}`
