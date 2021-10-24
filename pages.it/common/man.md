# man

> Formatta e mostra pagine manuale.
> Maggiori informazioni: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- Mostra la pagina di manuale di un comando:

`man {{comando}}`

- Mostra la pagina di manuale per un comando dalla sezione 7:

`man {{7}} {{comando}}`

- Mostra il percorso in cui vengono cercate le pagine:

`man --path`

- Mostra la posizione di una pagina invece che la pagina stessa:

`man -w {{comando}}`

- Cerca pagine di manuale che contengano una certa stringa:

`man -k {{ricerca}}`
