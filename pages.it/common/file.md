# file

> Determina il tipo di file.
> Maggiori informazioni: <https://manned.org/file>.

- Fornisce una descrizione del tipo di file specificato. Funziona anche con file senza estensione:

`file {{nome_file}}`

- Controlla dentro un file zip e determina il tipo dei file in esso contenuti:

`file -z {{foo.zip}}`

- Permette a `file` di leggere file speciali o di dispositivo:

`file -s {{nome_file}}`

- Non si limita al primo tipo di file trovato; continua a leggere il file fino alla fine:

`file -k {{nome_file}}`

- Determina il tipo MIME di un file:

`file -i {{nome_file}}`
