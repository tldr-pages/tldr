# eject

> Scoateți cd-urile, dischetele și unitățile de bandă.
> Mai multe informaţii: <https://manned.org/eject>

- Afișează dispozitivul implicit:

`eject -d`

- Scoateți dispozitivul implicit:

`eject`

- Scoateți un anumit dispozitiv (ordinea implicită este cd-rom, scsi, floppy și bandă):

`eject {{/dev/cdrom}}`

- Comutați dacă tava unui dispozitiv este deschisă sau închisă:

`eject -T {{/dev/cdrom}}`

- Ejectează o unitate CD:

`eject -r {{/dev/cdrom}}`

- Ejectează o unitate floppy:

`eject -f {{/mnt/floppy}}`

- Scoateți o unitate de bandă:

`eject -q {{/mnt/tape}}`
