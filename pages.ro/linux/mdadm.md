# mdadm

> Utilitar de gestionare RAID.
> Mai multe informaţii: <https://manned.org/mdadm>

- Creează matrice:

`mdadm --create {{/dev/md/MyRAID}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{/dev/sdXN}}`

- Stop array:

`mdadm --stop {{/dev/md0}}`

- Marcați discul ca nu a reușit:

`mdadm --fail {{/dev/md0}} {{/dev/sdXN}}`

- Scoateți discul:

`mdadm --remove {{/dev/md0}} {{/dev/sdXN}}`

- Adaugă disc la matrice:

`mdadm --assemble {{/dev/md0}} {{/dev/sdXN}}`

- Arată informaţii RAID:

`mdadm --detail {{/dev/md0}}`
