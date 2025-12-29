# bat

> Stampa e concatena file.
> Un clone di `cat` con syntax highlighting e integrazione Git.
> Maggiori informazioni: <https://manned.org/bat>.

- Stampa in modo formattato i contenuti di uno o più file su `stdout`:

`bat {{percorso/del/file1 percorso/del/file2 ...}}`

- Concatena diversi file nel file di destinazione:

`bat {{percorso/del/file1 percorso/del/file2 ...}} > {{percorso/del/file_destinazione}}`

- Rimuove decorazioni e disabilita paging (`--style plain` può essere sostituito con `-p`, o entrambe le opzioni con `-pp`):

`bat --style plain --pager never {{percorso/del/file}}`

- Evidenzia una riga specifica o un intervallo di righe con un colore di sfondo diverso:

`bat {{-H|--highlight-line}} {{10|5:10|:10|10:|10:+5}} {{percorso//del/file}}`

- Mostra caratteri non stampabili come spazio, tab o newline:

`bat {{-A|--show-all}} {{percorso/del/file}}`

- Rimuove tutte le decorazioni tranne i numeri di riga nell'output:

`bat {{-n|--number}} {{percorso/del/file}}`

- Evidenzia la sintassi di un file JSON impostando esplicitamente il linguaggio:

`bat {{-l|--language}} json {{percorso/del/file.json}}`

- Visualizza tutti i linguaggi supportati:

`bat {{-L|--list-languages}}`
