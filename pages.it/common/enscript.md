# enscript

> Converti file di testo in PostScript, HTML, RTF, ANSI ed overstrike.
> Maggiori informazioni: <https://www.gnu.org/software/enscript>.

- Genera un file PostScript da un file di testo:

`enscript {{percorso/del/file_input}} --output={{percorso/del/file_output}}`

- Genera un file in un linguaggio differente da PostScript:

`enscript {{percorso/del/file_input}} --language={{linguaggio}} --output={{percorso/del/file_output}}`

- Genera un file PostScript con layout orizzontale, dividendo la pagina in colonne (massimo 9):

`enscript {{percorso/del/file_input}} --columns={{numero_colonne}} --landscape --output={{percorso/del/file_output}}`

- Mostra linguaggi e formati file disponibili per evidenziare la sintassi:

`enscript --help-highlight`

- Genera un file PostScript con evidenziazione della sintassi e colori per uno specifico linguaggio:

`enscript {{percorso/del/file_input}} --color=1 --highlight={{linguaggio}} --output={{percorso/del/file_output}}`
