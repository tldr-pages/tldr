# pio package

> A csomagok kezelése a nyilvántartásban. A csomagok csak a közzétételük napjától számított 72 órán (3 napon) belül távolíthatók el. További információ: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- Csomagok tarballjának létrehozása az aktuális könyvtárból:

`pio package pack --output {{path/to/package.tar.gz}}`

- Csomag tarball létrehozása és közzététele az aktuális könyvtárból:

`pio package publish`

- Az aktuális könyvtár közzététele és a nyilvános hozzáférés korlátozása:

`pio package publish --private`

- Egy csomag közzététele:

`pio package publish {{path/to/package.tar.gz}}`

- Csomag közzététele egyéni kiadási dátummal (UTC):

`pio package publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- Egy közzétett csomag összes verziójának eltávolítása a nyilvántartásból:

`pio package unpublish {{package_name}}`

- Egy közzétett csomag egy adott verziójának eltávolítása a nyilvántartásból:

`pio package unpublish {{package_name}}@{{version}}`

- Az eltávolítás visszavonása, a csomag összes verziójának vagy egy adott verziójának visszahelyezése a rendszerleíró adatbázisba:

`pio package unpublish --undo {{package_name}}@{{version}}`
