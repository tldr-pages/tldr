# mount

> Fornisce accesso a un intero filesystem in una directory specifica.
> Maggiori informazioni: <https://manned.org/mount.8>.

- Mostra tutti i filesystem montati:

`mount`

- Monta un dispositivo in una directory:

`mount -t {{tipo_di_filesystem}} {{percorso/del/dispositivo}} {{percorso/della/directory_desiderata}}`

- Monta un CD-ROM (con il filetypo ISO9660) a `/cdrom` (sola lettura):

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- Monta tutti i filesystem definiti in `/etc/fstab`:

`mount -a`

- Monta un filesystem specifico descritto in `/etc/fstab` (ad esempio `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/my_drive}}`

- Monta una directory in un'altra directory:

`mount --bind {{percorso/della/vecchia_directory}} {{percorso/della/nuova_directory}}`
