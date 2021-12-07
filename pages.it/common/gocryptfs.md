# gocryptfs

> Filesystem crittografato scritto in Go.
> Maggiori informazioni: <https://github.com/rfjakob/gocryptfs>.

- Inizializzare un filesystem crittografato:

`gocryptfs -init {{percorso/al/cifrata}}`

- Montare un filesystem crittografato:

`gocryptfs {{percorso/cartella/cifrata}} {{percorso/punto/di/mount}}`

- Montare un filesystem usando la master key invece della password:

`gocryptfs --masterkey {{percorso/cartella/cifrata}} {{percorso/punto/di/mount}}`

- Cambiare la password:

`gocryptfs --passwd {{percorso/cartella/cifrata}}`

- Generare uno snapshot cifrato di una cartella:

`gocryptfs --reverse {{percorso/al/directory}} {{percorso/cartella/cifrata}}`
