# chown

> Cambia utente e gruppo proprietario di file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chown>.

- Cambia l'utente proprietario di un file/cartella:

`chown {{utente}} {{percorso/del/file_o_cartella}}`

- Cambia utente e gruppo proprietari di un file/cartella:

`chown {{utente}}:{{gruppo}} {{percorso/del/file_o_cartella}}`

- Cambia ricorsivamente il proprietario di una cartella ed i suoi contenuti:

`chown -R {{utente}} {{percorso/alla/cartella}}`

- Cambia il proprietario di un link simbolico:

`chown -h {{utente}} {{percorso/al/link_simbolico}}`

- Cambia il proprietario di un file/cartella rendendolo uguale a quello di un altro file di riferimento:

`chown --reference={{percorso/del/file_riferimento}} {{percorso/del/file_o_cartella}}`
