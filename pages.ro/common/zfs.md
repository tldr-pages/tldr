# zfs

> Gestionați sistemele de fișiere ZFS.

- Listează toate sistemele de fișiere zfs disponibile:

`zfs list`

- Creați un nou sistem de fișiere ZFS:

`zfs create {{pool_name/filesystem_name}}`

- Ștergeți un sistem de fișiere ZFS:

`zfs destroy {{pool_name/filesystem_name}}`

- Creați un instantaneu al unui sistem de fișiere ZFS:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Activați compresia pe un sistem de fișiere:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Schimbați punctul de montare pentru un sistem de fișiere:

`zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}`
