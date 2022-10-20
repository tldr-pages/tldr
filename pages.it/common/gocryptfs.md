# gocryptfs

> Filesystem crittografato scritto in Go.
> Maggiori informazioni: <https://github.com/rfjakob/gocryptfs>.

- Inizializzare un filesystem crittografato:

`gocryptfs -init {{percorso/del/cifrata}}`

- Montare un filesystem crittografato:

`gocryptfs {{percorso/directory/cifrata}} {{percorso/punto/di/mount}}`

- Montare un filesystem usando la master key invece della password:

`gocryptfs --masterkey {{percorso/directory/cifrata}} {{percorso/punto/di/mount}}`

- Cambiare la password:

`gocryptfs --passwd {{percorso/directory/cifrata}}`

- Generare uno snapshot cifrato di una directory:

`gocryptfs --reverse {{percorso/della/directory}} {{percorso/directory/cifrata}}`
