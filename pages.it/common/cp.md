# cp

> Copia file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/cp>.

- Copia un file in un'altra posizione:

`cp {{percorso/del/file}} {{percorso/della/copia}}`

- Copia un file in una cartella mantenendo il nome:

`cp {{percorso/del/file}} {{percorso/della/cartella}}`

- Copia una cartella ricorsivamente in un'altra posizione:

`cp -r {{percorso/della/cartella}} {{percorso/della/copia}}`

- Copia una cartella ricorsivamente in modo verboso (mostra a schermo ogni file copiato):

`cp -vr {{percorso/della/cartella}} {{percorso/della/copia}}`

- Copia i contenuti di una cartella in una seconda cartella:

`cp -r {{percorso/della/cartella/*}} {{percorso/della/seconda/cartella}}`

- Copia tutti i file di testo in una seconda cartella in modo interattivo (chiede conferma prima di sovrascrivere):

`cp -i {{*.txt}} {{percorso/della/cartella}}`
