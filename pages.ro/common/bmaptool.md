# bmaptool

> Creați sau copiați hărți bloc inteligent (concepute pentru a fi mai rapide decât `cp` sau `dd`).
> Mai multe informaţii: <https://source.tizen.org/documentation/reference/bmaptool>

- Creați un blockmap din fișierul imagine:

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- Copiați un fișier imagine în sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- Copiați un fișier imagine comprimat în sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- Copiați un fișier imagine în sdb fără a utiliza un blockmap:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`
