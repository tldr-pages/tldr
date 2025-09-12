# mount

> Krijg toegang tot een volledig bestandssysteem in één map.
> Meer informatie: <https://manned.org/mount.8>.

- Toon alle gemounte bestandssystemen:

`mount`

- Koppel een apparaat aan een map:

`mount {{pad/naar/apparaatbestand}} {{pad/naar/doelmap}}`

- Maak een specifieke map aan als het niet bestaat en koppel er een apparaat aan:

`mount {{[-m|--mkdir]}} {{pad/naar/apparaatbestand}} {{pad/naar/doelmap}}`

- Koppel een apparaat aan een map voor een specifieke gebruiker:

`mount {{[-o|--options]}} uid={{gebruiker_id}},gid={{groep_id}} {{pad/naar/apparaatbestand}} {{pad/naar/doelmap}}`

- Koppel een CD-ROM-apparaat (met bestandstype ISO9660) aan `/cdrom` (alleen-lezen):

`mount {{[-t|--types]}} iso9660 {{[-o|--options]}} ro {{/dev/cdrom}} /cdrom`

- Koppel alle bestandssystemen die gedefinieerd zijn in `/etc/fstab`:

`mount {{[-a|--all]}}`

- Koppel een specifiek bestandssysteem omschreven in `/etc/fstab` (b.v. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/mijn_schijf}}`

- Koppel een map aan een andere map:

`mount {{[-B|--bind]}} {{pad/naar/oude_map}} {{pad/naar/nieuwe_map}}`
