# tac

> Visualizza e concatena file con righe in ordine inverso.
> Guarda anche: `cat`.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/tac>.

- Concatena file specifici in ordine inverso:

`tac {{percorso/del/file1 percorso/del/file2 ...}}`

- Visualizza 'stdin' in ordine inverso:

`{{cat percorso/del/file}} | tac`

- Usa un [s]riparatore specifico:

`tac -s {{separatore}} {{percorso/del/file1 percorso/del/file2 ...}}`

- Usa un [r]egex specifico come [s]eparatore:

`tac -r -s {{separatore}} {{percorso/del/file1 percorso/del/file2 ...}}`

- Utilizzare un separatore [b]prima di ciascun file:

`tac -b {{percorso/del/file1 percorso/del/file2 ...}}`
