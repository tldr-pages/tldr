# extrace

> Az exec() hívások nyomon követése. További információ: <https://github.com/chneukirchen/extrace>.

- Nyomon követi a rendszerben futó összes programvégrehajtást:

`sudo extrace`

- Futtasson egy parancsot, és csak a parancs leszármazottait kövesse nyomon:

`sudo extrace {{command}}`

- Nyomtassa ki az egyes folyamatok aktuális munkakönyvtárát:

`sudo extrace -d`

- Az egyes futtatható programok teljes elérési útvonalának feloldása:

`sudo extrace -l`

- Az egyes folyamatokat futtató felhasználó megjelenítése:

`sudo extrace -u`
