# bmaptool

> Create or Copy blockmaps intelligently (and therefore faster than `cp` or `dd`).

- Create a blockmap from image file:

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- Copy an image file into sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- Copy a compressed image file into sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- Copy an image file into sdb without using a blockmap:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`
