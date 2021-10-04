# mount

> Fornisce accesso a un intero filesystem in una cartella specifica.
> Maggiori informazioni: <https://manned.org/mount.8>.

- Mostra tutti i filesystem montati:

`mount`

- Monta un dispositivo in una cartella:

`mount -t {{tipo_di_filesystem}} {{percorso/al/dispositivo}} {{percorso/alla/cartella_desiderata}}`

- Monta un CD-ROM (con il filetypo ISO9660) a `/cdrom` (sola lettura):

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- Monta tutti i filesystem definiti in `/etc/fstab`:

`mount -a`

- Monta un filesystem specifico descritto in `/etc/fstab` (ad esempio `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/my_drive}}`

- Monta una cartella in un'altra cartella:

`mount --bind {{percorso/alla/vecchia_cartella}} {{percorso/alla/nuova_cartella}}`
