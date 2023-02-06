# fakeroot

> Fájlmanipulációhoz szükséges parancs futtatása root jogosultságokat színlelő környezetben. További információ: <https://manpages.debian.org/latest/fakeroot/fakeroot.1.html>.

- Indítsa el az alapértelmezett héjat fakerootként:

`fakeroot`

- Futtasson egy parancsot fakeroot-ként:

`fakeroot -- {{command}} {{command_arguments}}`

- Futtasson parancsot fakerootként, és kilépéskor mentse a környezetet egy fájlba:

`fakeroot -s {{path/to/file}} -- {{command}} {{command_arguments}}`

- A fakeroot környezet betöltése és egy parancs fakeroot-ként történő futtatása:

`fakeroot -i {{path/to/file}} -- {{command}} {{command_arguments}}`

- Egy parancs futtatása a fájlok valódi tulajdonjogának megtartása helyett, ahelyett, hogy úgy tennénk, mintha a root tulajdonában lennének:

`fakeroot --unknown-is-real -- {{command}} {{command_arguments}}`

- Súgó megjelenítése:

`fakeroot --help`
