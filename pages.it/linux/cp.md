# cp

> Copia file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/cp>.

- Copia un file in un'altra posizione:

`cp {{persorso/al/file_da_copiare.est}} {{percorso/del/file_di_destinazione.est}}`

- Copia un file all'interno di una cartella, mantenendone uguale il nome:

`cp {{percorso/del/file_da_copiare.est}} {{percorso/alla/cartella}}`

- Copia ricorsivamente i contenuti di una cartella in un'altra posizione (se la destinazione esiste, la cartella è copiata al suo interno):

`cp -r {{percorso/alla/cartella_da_copiare}} {{percorso/di/destinazione}}`

- Copia una cartella ricorsivamente in modalità prolissa (mostra i file mentre vengono copiati):

`cp -vr {{percorso/alla/cartella_da_copiare}} {{percorso/di/destinazione}}`

- Copia i file di testo in un'altra posizione, in modalità interattiva (richiede conferma all'utente prima di sovrascrivere):

`cp -i {{*.txt}} {{percorso/di/destinazione}}`

- Segue i collegamenti simbolici prima di copiare:

`cp -L {{collegamento}} {{percorso/di/destinazione}}`

- Utilizza il percorso completo dei file originali, creando ogni cartella intermedia mancante mentre durante la copia:

`cp --parents {{percorso/dei/file/da/copiare}} {{percorso/del/file/destinazione}}`
