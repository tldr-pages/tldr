# autoflake

> Uno strumento per rimuovere import e variabili inutilizzati da codice Python.
> Maggiori informazioni: <https://github.com/myint/autoflake>.

- Rimuovi le variabili inutilizzate da un file e mostra la differenza:

`autoflake --remove-unused-variables {{percorso/del/file.py}}`

- Rimuovi gli import inutilizzati da multipli file mostrando le differenze:

`autoflake --remove-all-unused-imports {{percorso/del/file1.py percorso/del/file2.py ...}}`

- Rimuovi le variabili inutilizzate da un file, sovrascrivendolo:

`autoflake --remove-unused-variables --in-place {{percorso/del/file.py}}`

- Rimuovi le variabili inutilizzate da tutti i file in una directory, ricorsivamente e sovrascrivendoli:

`autoflake --remove-unused-variables --in-place --recursive {{percorso/della/directory}}`
