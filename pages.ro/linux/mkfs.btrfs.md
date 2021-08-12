# mkfs.btrfs

> Creați un sistem de fișiere btrfs.
> Implicit la `raid1”, care specifică 2 copii ale unui anumit bloc de date răspândit pe 2 dispozitive diferite.
> Mai multe informaţii: <https://btrfs.wiki.kernel.org/index.php/Manpage/mkfs.btrfs>

- Creați un sistem de fișiere btrfs pe un singur dispozitiv:

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- Creați un sistem de fișiere btrfs pe mai multe dispozitive cu raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- Setați o etichetă pentru sistemul de fișiere:

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`
