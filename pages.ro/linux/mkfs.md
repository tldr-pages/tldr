# mkfs

> Construiți un sistem de fișiere Linux pe o partiție de hard disk.
> Această comandă este învechită în favoarea mkfs specifice sistemului de fișiere. <type> Utils.

- Construiește un sistem de fișiere Linux ext2 pe o partiție:

`mkfs {{path/to/partition}}`

- Construiți un sistem de fișiere de un tip specificat:

`mkfs -t {{ext4}} {{path/to/partition}}`

- Construiți un sistem de fișiere de un tip specificat și verificați blocurile necorespunzătoare:

`mkfs -c -t {{ntfs}} {{path/to/partition}}`
