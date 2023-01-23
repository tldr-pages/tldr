# ipfs

> Inter Planetary File System: Egy egyenrangú hipermédia protokoll. Célja a web nyitottabbá tétele. További információ: <https://ipfs.io>.

- Hozzáad egy fájlt a helyi fájlrendszerhez, kitűzi és kiírja a relatív hash-t:

`ipfs add {{path/to/file}}`

- Egy könyvtár és a benne lévő fájlok rekurzív módon történő hozzáadása a helyi fájlrendszerhez, és a relatív hash kiírása:

`ipfs add -r {{path/to/directory}}`

- Távoli fájl mentése és nevének megadása, de nem tűzi ki:

`ipfs get {{hash}} -o {{path/to/file}}`

- Távoli fájl helyi kitűzése:

`ipfs pin add {{hash}}`

- A kitűzött fájlok megjelenítése:

`ipfs pin ls`

- Egy fájl kitapasztásának feloldása a helyi tárolóból:

`ipfs pin rm {{hash}}`

- Tűzetlen fájlok eltávolítása a helyi tárolóból:

`ipfs repo gc`
