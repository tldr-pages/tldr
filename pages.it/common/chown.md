# chown

> Cambia utente e gruppo proprietario di file e directory.

- Cambia l'utente proprietario di un file/directory:

`chown {{utente}} {{percorso/a/file_o_directory}}`

- Cambia utente e gruppo proprietari di un file/directory:

`chown {{utente}}:{{gruppo}} {{percorso/a/file_o_directory}}`

- Cambia ricorsivamente il proprietario di una cartella ed i suoi contenuti:

`chown -R {{utente}} {{percorso/alla/directory}}`

- Cambia il proprietario di un link simbolico:

`chown -h {{utente}} {{percorso/al/link_simbolico}}`

- Cambia il proprietario di un file/directory rendendolo uguale a quello di un altro file di riferimento:

`chown --reference={{percorso/al/file_riferimento}} {{percorso/a/file_o_directory}}`
