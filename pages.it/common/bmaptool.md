# bmaptool

> Crea o copia blockmap intelligentemente (e quindi più velocemente di `cp` o `dd`).
> Maggiori informazioni: <https://manned.org/bmaptool>.

- Crea una blockmap da un file immagine:

`bmaptool create -o {{blockmap.bmap}} {{sorgente.img}}`

- Copia un file immagine su sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{sorgente.img}} {{/dev/sdb}}`

- Copia un file immagine compresso su sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{sorgente.img.gz}} {{/dev/sdb}}`

- Copia un file immagine su sdb senza utilizzare una blockmap:

`bmaptool copy --nobmap {{sorgente.img}} {{/dev/sdb}}`
