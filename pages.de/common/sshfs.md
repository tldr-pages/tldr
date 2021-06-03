# sshfs

> Dateisystem Client für SSH.
> Weitere Informationen: <https://github.com/libfuse/sshfs>.

- Hänge ein externes Verzeichnis ein:

`sshfs {{benutzer}}@{{externer_server}}:{{externes_verzeichnis}} {{lokales_einhänge_verzeichnis}}`

- Hänge ein externes Verzeichnis aus:

`umount {{lokaler_einhänge_verzeichnis}}`

- Hänge ein externes Verzeichnis unter einem bestimmten Port ein:

`sshfs {{benutzer}}@{{externer_server}}:{{externes_verzeichnis}} -p {{2222}}`

- Verwende Komprimierung:

`sshfs {{benutzer}}@{{externer_server}}:{{externes_verzeichnis}} -C`

- Folge symbolischen Links:

`sshfs -o follow_symlinks {{benutzer}}@{{externer_server}}:{{externes_verzeichnis}} {{lokaler_einhänge_verzeichnis}}`
