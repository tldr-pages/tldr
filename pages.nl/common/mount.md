# mount

> Krijg toegang tot een volledig bestandssysteem in één directory.
> Meer informatie: <https://manned.org/mount.8>.

- Toon alle aangekoppelde bestandssystemen:

`mount`

- Koppel een apparaat aan een directory:

`mount {{[-t|--types]}} {{bestandssysteem_type}} {{pad/naar/apparaatbestand}} {{pad/naar/doelmap}}`

- Maak een specifieke directory als deze niet bestaat en koppel een apparaat eraan:

`mount {{[-m|--mkdir]}} {{pad/naar/apparaatbestand}} {{pad/naar/doelmap}}`

- Koppel een apparaat aan een directory voor een specifieke gebruiker:

`mount {{[-o|--options]}} uid={{gebruiker_id}},gid={{groep_id}} {{pad/naar/apparaatbestand}} {{pad/naar/doelmap}}`

- Koppel een CD-ROM-apparaat (met het bestandstype ISO9660) aan `/cdrom` (alleen-lezen):

`mount {{[-t|--types]}} {{iso9660}} {{[-o|--options]}} ro {{/dev/cdrom}} {{/cdrom}}`

- Koppel alle bestandssystemen die zijn gedefinieerd in `/etc/fstab`:

`mount {{[-a|--all]}}`

- Koppel een specifiek bestandssysteem zoals beschreven in `/etc/fstab` (bijv. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/my_drive}}`

- Koppel een directory aan een andere directory:

`mount {{[-B|--bind]}} {{pad/naar/oude_map}} {{pad/naar/nieuwe_map}}`
