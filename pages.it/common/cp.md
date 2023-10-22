# cp

> Copia file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/cp>.

- Copia un file in un'altra posizione:

`cp {{percorso/del/file}} {{percorso/della/copia}}`

- Copia un file in una directory mantenendo il nome:

`cp {{percorso/del/file}} {{percorso/della/directory}}`

- Copia una directory ricorsivamente in un'altra posizione:

`cp -r {{percorso/della/directory}} {{percorso/della/copia}}`

- Copia una directory ricorsivamente in modo verboso (mostra a schermo ogni file copiato):

`cp -vr {{percorso/della/directory}} {{percorso/della/copia}}`

- Copia i contenuti di una directory in una seconda directory:

`cp -r {{percorso/della/directory/*}} {{percorso/della/seconda/directory}}`

- Copia tutti i file di testo in una seconda directory in modo interattivo (chiede conferma prima di sovrascrivere):

`cp -i {{*.txt}} {{percorso/della/directory}}`
