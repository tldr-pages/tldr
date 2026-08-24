# cat

> Stampa e concatena file.
> Maggiori informazioni: <https://manned.org/cat.1posix>.

- Stampa il contenuto di un file su `stdout`:

`cat {{percorso/del/file}}`

- Concatena diversi file in un file di output:

`cat {{percorso/del/file1 percorso/del/file2 ...}} > {{percorso/del/file_di_output}}`

- Aggiunge diversi file a un file di output:

`cat {{percorso/del/file1 percorso/del/file2 ...}} >> {{percorso/del/file_di_output}}`

- Copia il contenuto di un file in un file di output senza buffering:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Scrive `stdin` in un file:

`cat - > {{percorso/del/file}}`
