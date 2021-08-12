# pmount

> Montați dispozitive hotpluggable arbitrare ca utilizator normal.
> Mai multe informaţii: <https://manned.org/pmount>

- Montați un dispozitiv sub `/media/` (folosind dispozitivul ca punct de montare):

`pmount {{/dev/to/block/device}}`

- Montați un dispozitiv cu un anumit tip de sistem de fișiere la `/media/etichetă':

`pmount --type {{filesystem}} {{/dev/to/block/device}} {{label}}`

- Montează un CD-ROM (tip sistem de fișiere ISO9660) în modul doar în citire:

`pmount --type {{iso9660}} --read-only {{/dev/cdrom}}`

- Montați un disc formatat NTFS, forțând accesul citire-scriere:

`pmount --type {{ntfs}} --read-write {{/dev/sdX}}`

- Afișează toate dispozitivele amovibile montate:

`pmount`
