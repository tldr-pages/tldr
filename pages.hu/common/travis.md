# travis

> Parancssori kliens a Travis CI-vel való kapcsolathoz. További információ: <https://github.com/travis-ci/travis.rb>.

- A kliens verziójának megjelenítése:

`travis version`

- Hitelesítse a CLI-ügyfelet a kiszolgálóval szemben egy hitelesítési token segítségével:

`travis login`

- Listázza ki azokat a tárolókat, amelyekhez a felhasználónak jogosultsága van:

`travis repos`

- Az értékek titkosítása a `.travis.yml` oldalon:

`travis encrypt {{token}}`

- Generáljon egy `.travis.yml` fájlt és engedélyezze a projektet:

`travis init`
