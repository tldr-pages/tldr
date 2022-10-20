# chown

> Cambia utente e gruppo proprietario di file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chown>.

- Cambia l'utente proprietario di un file/directory:

`chown {{utente}} {{percorso/del/file_o_directory}}`

- Cambia utente e gruppo proprietari di un file/directory:

`chown {{utente}}:{{gruppo}} {{percorso/del/file_o_directory}}`

- Cambia ricorsivamente il proprietario di una directory ed i suoi contenuti:

`chown -R {{utente}} {{percorso/della/directory}}`

- Cambia il proprietario di un link simbolico:

`chown -h {{utente}} {{percorso/del/link_simbolico}}`

- Cambia il proprietario di un file/directory rendendolo uguale a quello di un altro file di riferimento:

`chown --reference={{percorso/del/file_riferimento}} {{percorso/del/file_o_directory}}`
