# dirname

> Determina la directory genitore di un determinato file o percorso.

- Calcola la directory genitore di un dato percorso:

`dirname {{percorso/a/file_o_directory}}`

- Calcola la directory genitore di più percorsi:

`dirname {{percorso/a/file_a}} {{percorso/a/directory_b}}`

- Delimita l'output con caratteri NUL invece di newline (utile in combinazione con `xargs`):

`dirname --zero {{percorso/a/directory_a}} {{percorso/a/file_b}}`
