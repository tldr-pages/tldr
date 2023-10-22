# mount

> Ermöglicht den Zugriff auf ein gesamtes Dateisystem in einem Verzeichnis.
> Weitere Informationen: <https://manned.org/mount.8>.

- Zeige alle eingehängten Dateisysteme:

`mount`

- Hänge ein Gerät in ein Verzeichnis ein:

`mount -t {{dateisystemtyp}} {{pfad/zu/gerätedatei}} {{pfad/zu/zielverzeichnis}}`

- Hänge ein CD-ROM-Gerät (Dateisystemtyp ISO9660) in das Verzeichnis `/cdrom` schreibgeschützt ein:

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- Hänge alle Dateisysteme ein, die in `/etc/fstab` definiert sind:

`mount -a`

- Hänge ein Dateisystem ein, das in `/etc/fstab` beschrieben ist (z. B. `/dev/sda1 /meine_platte ext2 defaults 0 2`):

`mount {{/meine_platte}}`

- Hänge ein Verzeichnis in ein anderes Verzeichnis ein (danach sind die Inhalte über beide Pfade verfügbar):

`mount --bind {{pfad/zu/altem_verzeichnis}} {{pfad/zu/neuem_verzeichnis}}`
