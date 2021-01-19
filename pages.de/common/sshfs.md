# sshfs

> Dateisystem Client für SSH.
> Mehr Informationen: <https://github.com/libfuse/sshfs>.

- Einhängen eines externen Ordners:

`sshfs {{Benutzer}}@{{Externer_Server}}:{{Externer_Ordner}} {{Lokaler_Einhänguns_Ordner}}`

- Aushängen eines externen Ordners:

`umount {{Lokaler_Einhängungs_Ordner}}`

- Einhängen eines externen Ordners unter einem bestimmten Port:

`sshfs {{Benutzer}}@{{Externer_Server}}:{{Externer_Ordner}} -p {{2222}}`

- Einsatz von Komprimierung:

`sshfs {{Benutzer}}@{{Externer_Server}}:{{Externer_Ordner}} -C`

- Beachtung symbolischer Verweise:

`sshfs -o follow_symlinks {{Benutzer}}@{{Externer_Server}}:{{Externer_Ordner}} {{Lokaler_Einhängungs_Ordner}}`
