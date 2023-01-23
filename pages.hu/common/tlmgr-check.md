# tlmgr check

> A TeX Live telepítés konzisztenciájának ellenőrzése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- A teljes TeX Live telepítés konzisztenciájának ellenőrzése:

`tlmgr check all`

- A teljes TeX Live információ konzisztenciájának ellenőrzése verbózus üzemmódban:

`tlmgr check all -v`

- A hiányzó függőségek ellenőrzése:

`tlmgr check depends`

- Ellenőrizze, hogy az összes TeX Live futtatható fájl jelen van-e:

`tlmgr check executes`

- Ellenőrizze, hogy a helyi TLPDB-ben felsorolt összes fájl jelen van-e:

`tlmgr check files`

- Ellenőrizze a duplikált fájlneveket a runfiles szakaszokban:

`tlmgr check runfiles`
