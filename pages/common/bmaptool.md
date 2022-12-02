# bmaptool

> Create or copy block maps intelligently (designed to be faster than `cp` or `dd`).
> More information: <https://source.tizen.org/documentation/reference/bmaptool>.

- Create a blockmap from image file:

`bmaptool create -o {{blockmap.bmap}} {{path/to/source.img}}`

- Copy an image file into sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{path/to/source.img}} {{/dev/sdb}}`

- Copy a compressed image file into sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{path/to/source.gz}} {{/dev/sdb}}`

- Copy an image file into sdb without using a blockmap:

`bmaptool copy --nobmap {{path/to/source.img}} {{/dev/sdb}}`
