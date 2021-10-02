# mount

> Dateisyteme in Dateibaum einhängen

- Zeige alle eingehängten Dateisyteme:

`mount`

- Hänge ein Gerät (en. Device) in das Dateiverzeichnis ein:

`mount -t {{Dateisystemtyp}} {{pfad/zu/gerätedatei}} {{pfad/zu/zielverzeichnis}}`

- Hänge ein CD-ROM-Gerät, das unter `/dev/cdrom` liegt (Dateisystemtyp ISO9660), in das Verzeichnis `/cdrom` schreibgeschützt ein:

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- Hänge alle Dateisysteme ein die in `/etc/fstab` definiert sind:

`mount -a`

- Hänge ein Dateisystem, dessen Einhängepunkt, Dateisystemtyp und Optionen in der Dateisystemtabelle `/etc/fstab` beschrieben sind ein (z. B. `/dev/sda1 /meine_platte ext2 defaults 0 2`):

`mount {{/meine_platte}}`

- Hänge ein Verzeichnis an eine andere Stelle im Dateisystem, danach sind die Inhalte über beide Pfade verfügbar:

`mount --bind {{pfad/zu/altem_verzeichnis}} {{pfad/zu/neuem_verzeichnis}}`
