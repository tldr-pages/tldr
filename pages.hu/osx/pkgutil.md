# pkgutil

> A Mac OS X Installer csomagok és bizonylatok lekérdezése és kezelése. További információ: <https://ss64.com/osx/pkgutil.html>.

- Az összes telepített csomag csomagazonosítójának listázása:

`pkgutil --pkgs`

- Egy csomagfájl kriptográfiai aláírásának ellenőrzése:

`pkgutil --check-signature {{path/to/filename.pkg}}`

- Egy telepített csomag összes fájljának listázása az azonosítója alapján:

`pkgutil --files {{com.microsoft.Word}}`

- Egy csomagfájl tartalmának kivonása egy könyvtárba:

`pkgutil --expand-full {{path/to/filename.pkg}} {{path/to/directory}}`
