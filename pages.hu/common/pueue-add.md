# pueue add

> Egy feladat sorba állítása végrehajtásra. További információ: <https://github.com/Nukesor/pueue>.

- Bármely parancs hozzáadása az alapértelmezett várólistához:

`pueue add {{command}}`

- A sorba állításkor átadhatja a parancsnak a zászlók vagy argumentumok listáját:

`pueue add -- {{command --arg -f}}`

- Adjon hozzá egy parancsot, de ne indítsa el, ha az az első a sorban:

`pueue add --stashed -- {{rsync --archive --compress /local/directory /remote/directory}}`

- Adjon hozzá egy parancsot egy csoporthoz, és azonnal indítsa el, lásd: `pueue group` a csoportok kezeléséhez:

`pueue add --immediate --group "{{CPU_intensive}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- Adjon hozzá egy parancsot, és indítsa el a 9. és 12. parancsok sikeres befejezése után:

`pueue add --after {{9}} {{12}} --group "{{torrents}}" -- {{transmission-cli torrent_file.torrent}}`

- Adjon hozzá egy parancsot egy címkével, miután eltelt némi késleltetés, az érvényes dátumformátumokról lásd `pueue enqueue`:

`pueue add --label "{{compressing large file}}" --delay "{{wednesday 10:30pm}}" -- "{{7z a compressed_file.7z large_file.xml}}"`
