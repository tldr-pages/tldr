# gocryptfs

> Filesystem crittografato scritto in Go.
> Maggiori informazioni: <https://github.com/rfjakob/gocryptfs>.

- Inizializzare un filesystem crittografato:

`gocryptfs -init {{percorso/della/directory_cifrata}}`

- Montare un filesystem crittografato:

`gocryptfs {{percorso/della/directory_cifrata}} {{percorso/del/punto_di_mount}}`

- Montare un filesystem usando la master key invece della password:

`gocryptfs --masterkey {{percorso/della/directory_cifrata}} {{percorso/del/punto_di_mount}}`

- Cambiare la password:

`gocryptfs --passwd {{percorso/della/directory_cifrata}}`

- Generare uno snapshot cifrato di una directory:

`gocryptfs --reverse {{percorso/della/directory}} {{percorso/della/directory_cifrata}}`
