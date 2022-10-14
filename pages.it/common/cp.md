# cp

> Copia file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/cp>.

- Copia un file in un'altra posizione:

`cp {{percorso/al/file}} {{percorso/alla/copia}}`

- Copia un file in una cartella mantenendo il nome:

`cp {{percorso/al/file}} {{percorso/alla/cartella}}`

- Copia una cartella ricorsivamente in un'altra posizione:

`cp -r {{percorso/alla/cartella}} {{percorso/alla/copia}}`

- Copia una cartella ricorsivamente in modo verboso (mostra a schermo ogni file copiato):

`cp -vr {{percorso/alla/cartella}} {{percorso/alla/copia}}`

- Copia i contenuti di una cartella in una seconda cartella:

`cp -r {{percorso/alla/cartella/*}} {{percorso/alla/seconda/cartella}}`

- Copia tutti i file di testo in una seconda cartella in modo interattivo (chiede conferma prima di sovrascrivere):

`cp -i {{*.txt}} {{percorso/alla/cartella}}`
