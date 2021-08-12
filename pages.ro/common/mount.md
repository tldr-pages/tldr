# mount

> Oferă acces la un întreg sistem de fișiere într-un singur director.

- Afișează toate sistemele de fișiere montate:

`mount`

- Montați un dispozitiv într-un director:

`mount -t {{filesystem_type}} {{path/to/device_file}} {{path/to/target_directory}}`

- Montați un dispozitiv CD-ROM (cu tipul de fișier ISO9660) la `/cdrom` (readonly):

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- Montează tot sistemul de fișiere definit în `/etc/fstab`:

`mount -a`

- Montează un sistem de fișiere specific descris în `/etc/fstab` (de exemplu `/dev/sda1 /my_drive ext2 implicit 0 2`):

`mount {{/my_drive}}`

- Montați un director în alt director:

`mount --bind {{path/to/old_dir}} {{path/to/new_dir}}`
