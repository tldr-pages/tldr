# cat

> Stampa e concatena file.
> Maggiori informazioni: <https://manned.org/cat.1posix>.

- Stampa i contenuti di un file su `stdout`:

`cat {{percorso/del/file}}`

- Concatena più file in un unico file:

`cat {{percorso/del/file1 percorso/del/file2 ...}} > {{percorso/del/file_finale}}`

- Aggiungi il contenuto di diversi file alla fine di un file:

`cat {{percorso/del/file1 percorso/del/file2 ...}} >> {{percorso/del/file_finale}}`

- Copia il contenuto di un file in un file di output senza buffering:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Scrive `stdin` in un file:

`cat - > {{percorso/del/file}}`
