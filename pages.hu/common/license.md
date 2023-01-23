# license

> Licencfájlok létrehozása nyílt forráskódú projektekhez. További információ: <https://nishanths.github.io/license>.

- Nyomtasson ki egy licencet a `stdout` címre, az alapértelmezett beállítások (automatikus szerzői név és az aktuális év) használatával:

`license {{license_name}}`

- Licenc generálása és mentése egy fájlba:

`license -o {{path/to/file}} {{license_name}}`

- Az összes rendelkezésre álló licenc listázása:

`license ls`

- Licenc generálása egyéni szerzői névvel és évszámmal:

`license --name {{author}} --year {{release_year}} {{license_name}}`
