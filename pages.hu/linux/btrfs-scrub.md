# btrfs scrub

> A btrfs fájlrendszerek súrolása az adatok sértetlenségének ellenőrzésére. Ajánlott havonta egyszer lefuttatni a súrolást. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Indítsa el a scrub-ot:

`sudo btrfs scrub start {{path/to/btrfs_mount}}`

- Megjeleníti a folyamatban lévő vagy legutóbb befejezett törlés állapotát:

`sudo btrfs scrub status {{path/to/btrfs_mount}}`

- Folyamatban lévő törlés törlése:

`sudo btrfs scrub cancel {{path/to/btrfs_mount}}`

- Egy korábban leállított súrolás folytatása:

`sudo btrfs scrub resume {{path/to/btrfs_mount}}`

- Kezdjen el egy súrolást, de a kilépés előtt várjon a súrolás befejezéséig:

`sudo btrfs scrub start -B {{path/to/btrfs_mount}}`

- Vizsgálat indítása csendes üzemmódban (nem nyomtat hibákat vagy statisztikákat):

`sudo btrfs scrub start -q {{path/to/btrfs_mount}}`
