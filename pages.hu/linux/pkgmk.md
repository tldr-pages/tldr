# pkgmk

> Készítsen bináris csomagot a pkgadd segítségével a CRUX-on. További információ: <https://docs.oracle.com/cd/E19683-01/816-0210/6m6nb7mha/index.html>.

- Csomag készítése és letöltése:

`pkgmk -d`

- Telepítse a csomagot az elkészítés után:

`pkgmk -d -i`

- A csomag frissítése az elkészítés után:

`pkgmk -d -u`

- A csomag elkészítésekor figyelmen kívül hagyja a lábnyomot:

`pkgmk -d -if`

- Az MD5 összeg figyelmen kívül hagyása csomag készítésekor:

`pkgmk -d -im`

- A csomag lábnyomának frissítése:

`pkgmk -uf`
