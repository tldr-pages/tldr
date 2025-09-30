# dirname

> Determina la directory genitore di un determinato file o percorso.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Calcola la directory genitore di un dato percorso:

`dirname {{percorso/del/file_o_directory}}`

- Calcola la directory genitore di più percorsi:

`dirname {{percorso/del/file_or_directory1 percorso/del/file_or_directory2 ...}}`

- Delimita l'output utilizzando caratteri NUL invece di una nuova linea (utile in combinazione con `xargs`):

`dirname {{[-z|--zero]}} {{percorso/del/file_or_directory1 percorso/del/file_or_directory2 ...}}`
