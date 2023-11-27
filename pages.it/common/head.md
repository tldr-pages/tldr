# head

> Stampa a schermo le prime linee di un file.
> Maggiori informazioni: <https://manned.org/head.1p>.

- Stampa a schermo le prime linee di un file:

`head -n {{numero_di_linee}} {{file}}`

- Stampa a schermo i primi byte di un file:

`head -c {{numero_di_byte}} {{file}}`

- Stampa a schermo tutto il file meno le ultime linee:

`head -n -{{numero_di_linee}} {{file}}`

- Stampa a schermo tutto il file meno gli ultimi byte:

`head -c -{{numero_di_byte}} {{file}}`
