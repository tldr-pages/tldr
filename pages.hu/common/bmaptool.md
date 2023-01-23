# bmaptool

> Intelligens módon hozhat létre vagy másolhat blokktérképeket (gyorsabb, mint a `cp` vagy a `dd`). További információ: <https://source.tizen.org/documentation/reference/bmaptool>.

- Blokktérkép létrehozása képfájlból:

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- Másoljon egy képfájlt az sdb-be:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- Tömörített képfájl másolása az sdb-be:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- Képfájl másolása az sdb-be blockmap használata nélkül:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`
