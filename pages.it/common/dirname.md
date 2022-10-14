# dirname

> Determina la cartella genitore di un determinato file o percorso.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/dirname>.

- Calcola la cartella genitore di un dato percorso:

`dirname {{percorso/del/file_o_cartella}}`

- Calcola la cartella genitore di più percorsi:

`dirname {{percorso/del/file_a}} {{percorso/a/cartella_b}}`

- Delimita l'output con caratteri NUL invece di newline (utile in combinazione con `xargs`):

`dirname --zero {{percorso/a/cartella_a}} {{percorso/del/file_b}}`
