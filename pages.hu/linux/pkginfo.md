# pkginfo

> A CRUX rendszer csomagadatbázisának lekérdezése. További információ: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- A telepített csomagok és verzióik listázása:

`pkginfo -i`

- A csomaghoz tartozó fájlok listázása:

`pkginfo -l {{package_name}}`

- A mintának megfelelő fájlok tulajdonosának (tulajdonosainak) listázása:

`pkginfo -o {{pattern}}`

- Egy fájl lábnyomának kinyomtatása:

`pkginfo -f {{path/to/file}}`
