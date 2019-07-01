# cp

> Copia file e directory.

- Copia un file in un'altra posizione:

`cp {{percorso/al/file}} {{percorso/alla/copia}}`

- Copia un file in una directory mantenendo il nome:

`cp {{percorso/al/file}} {{percorso/alla/directory}}`

- Copia una directory ricorsivamente in un'altra posizione:

`cp -r {{percorso/alla/directory}} {{percorso/alla/copia}}`

- Copia una directory ricorsivamente in modo verboso (mostra a schermo ogni file copiato):

`cp -vr {{percorso/alla/directory}} {{percorso/alla/copia}}`

- Copia i contenuti di una directory in una seconda directory:

`cp -r {{percorso/alla/directory/*}} {{percorso/alla/seconda/directory}}`

- Copia tutti i file di testo in una seconda directory in modo interattivo  (chiede conferma prima di sovrascrivere):

`cp -i {{*.txt}} {{percorso/alla/directory}}`
