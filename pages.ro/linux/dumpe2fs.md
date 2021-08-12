# dumpe2fs

> Imprimați informațiile grupului super bloc și blocuri pentru sistemele de fișiere ext2/ext3/ext4.
> Demontați partiția înainte de a executa această comandă folosind `umount {{device}} `.
> Mai multe informaţii: <https://manned.org/dumpe2fs>

- Afișează informații despre sistemul de fișiere ext2, ext3 și ext4:

`dumpe2fs {{/dev/sdXN}}`

- Afișează blocurile care sunt rezervate la fel de rău în sistemul de fișiere:

`dumpe2fs -b {{/dev/sdXN}}`

- Forțați informațiile despre sistemul de fișiere de afișare chiar și cu semnalizatoare de caracteristici care nu pot fi recunoscute:

`dumpe2fs -f {{/dev/sdXN}}`

- Afișați numai informațiile superblock și nu oricare dintre informațiile detaliate descriptor grup bloc:

`dumpe2fs -h {{/dev/sdXN}}`

- Imprimați numerele detaliate ale blocului de informații de grup în format hexazecimal:

`dumpe2fs -x {{/dev/sdXN}}`
