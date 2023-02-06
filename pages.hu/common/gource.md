# gource

> A Git, SVN, Mercurial és Bazaar tárolók animált fadiagramját jeleníti meg. A létrehozott, módosított vagy eltávolított fájlokat és könyvtárakat mutatja az idő múlásával. További információ: <https://gource.io>.

- A gource futtatása egy könyvtárban (ha ez nem a tároló gyökérkönyvtára, akkor a gyökeret keresi meg onnan):

`gource {{path/to/repository}}`

- A gource futtatása az aktuális könyvtárban, egyéni kimeneti felbontással:

`gource -{{width}}x{{height}}`

- Állítson be egy egyéni időskálát az animációhoz:

`gource -c {{time_scale_multiplier}}`

- Állítsa be, hogy az egyes napok milyen hosszúak legyenek az animációban (ez kombinálható a -c-vel, ha megadva van):

`gource -s {{seconds}}`

- Teljes képernyős mód és egyéni háttérszín beállítása:

`gource -f -b {{hex_color_code}}`

- Az animáció címének beállítása:

`gource --title {{title}}`
