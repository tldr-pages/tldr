# virt-sparsify

> Faceți ca imaginile unității de mașină virtuală să fie subțiate.
> NOTĂ: Utilizați numai pentru mașinile offline pentru a evita deteriorarea datelor.
> Pagina de pornire: <https://libguestfs.org/>

- Creați o imagine comprimată îmbunătățită fără instantanee dintr-o imagine nesparsificată:

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/image_new.qcow2}}`

- Sparifica o imagine în loc:

`virt-sparsify --in-place {{path/to/image.img}}`
