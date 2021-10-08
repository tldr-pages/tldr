# box

> Una applicazione PHP per creare e gestire Phars.
> Maggiori informazioni: <https://github.com/box-project/box>.

- Crea un nuovo file Phar:

`box build`

- Crea un nuovo file Phar usando uno specifico file di configurazione:

`box build -c {{percorso/a/configurazione}}`

- Mostra informazioni sulla estensione PHP PHAR:

`box info`

- Mostra informazioni su di uno specifico file Phar:

`box info {{percorso/a/file_phar}}`

- Valida il primo file di configurazione trovato nella directory corrente:

`box validate`

- Verifica la firma di uno specifico file Phar:

`box verify {{percorso/a/file_phar}}`

- Mostra tutti i comandi ed opzioni disponibili:

`box help`
