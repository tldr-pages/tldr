# systemd-mount

> Maak tijdelijke mount- of auto-mountpunten aan en verwijder ze.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/systemd-mount.html>.

- Mount een bestandssysteem (image of blokapparaat) op `/run/media/system/LABEL` waar LABEL het bestandssysteemlabel is of de apparaatnaam als er geen label is:

`systemd-mount {{pad/naar/bestand_of_apparaat}}`

- Mount een bestandssysteem (image of blokapparaat) op een gegeven locatie:

`systemd-mount {{pad/naar/bestand_of_apparaat}} {{pad/naar/mountpunt}}`

- Toon een lijst van alle lokale, bekende blokapparaten met de bestandssystemen die mogelijk gemount kunnen worden:

`systemd-mount --list`

- Maak een auto-mountpunt dat het daadwerkelijke bestandssysteem zal mounten op het moment van eerste toegang:

`systemd-mount --automount yes {{pad/naar/bestand_of_apparaat}}`

- Unmount een of meerdere apparaten:

`systemd-mount {{[-u|--umount]}} {{pad/naar/mountpunt_of_apparaat1 pad/naar/mountpunt_of_apparaat2 ...}}`

- Mount een bestandssysteem (image of blokapparaat) met een specifiek bestandssysteemtype:

`systemd-mount {{[-t|--type]}} {{bestandssysteemtype}} {{pad/naar/bestand_of_apparaat}} {{pad/naar/mountpunt}}`

- Mount een bestandssysteem (image of blokapparaat) met extra mount-opties:

`systemd-mount {{[-o|--options]}} {{mount_opties}} {{pad/naar/bestand_of_apparaat}} {{pad/naar/mountpunt}}`
