# systemd-mount

> Zet mount of auto-mount punten op of verwijder ze.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemd-mount.html>.

- Mount een bestandssysteem (afbeelding of blokapparaat) op `/run/media/system/LABEL` waar LABEL het bestandssysteemlabel is of de apparaatnaam als er geen label is:

`systemd-mount {{pad/naar/bestand_of_apparaat}}`

- Mount een bestandssysteem (afbeelding of blokapparaat) op een gegeven locatie:

`systemd-mount {{pad/naar/bestand_of_apparaat}} {{pad/naar/mount_point}}`

- Toon een lijst van alle lokale, bekende blokapparaten met de bestandssystemen die mogelijk gemount kunnen worden:

`systemd-mount --list`

- Maak een automount punt dat het bestandssysteem zal mounten op het moment van eerste toegang:

`systemd-mount --automount=yes {{pad/naar/bestand_of_apparaat}}`

- Unmount een of meerdere apparaten:

`systemd-mount --umount {{pad/naar/mount_point_of_apparaat1}} {{pad/naar/mount_point_of_apparaat2}}`

- Mount een bestandssysteem (afbeelding of blokapparaat) met een specifiek bestandssysteemtype:

`systemd-mount --type={{file_system_type}} {{pad/naar/bestand_of_apparaat}} {{pad/naar/mount_point}}`

- Mount een bestandssysteem (afbeelding of blokapparaat) met extra mount opties:

`systemd-mount --options={{mount_options}} {{pad/naar/bestand_of_apparaat}} {{pad/naar/mount_point}}`
