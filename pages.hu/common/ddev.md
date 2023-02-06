# ddev

> Konténer alapú helyi fejlesztőeszköz PHP környezetekhez. További információ: <https://ddev.readthedocs.io>.

- Projekt indítása:

`ddev start`

- A projekt típusának és docroot-jának beállítása:

`ddev config`

- \[f\]ollow the log trail:

`ddev logs -f`

- Futtassa a composert a konténeren belül:

`ddev composer`

- Egy adott Node.js verzió telepítése:

`ddev nvm install {{version}}`

- Exportáljon egy adatbázist:

`ddev export-db --file={{/tmp/db.sql.gz}}`

- Egy adott parancs futtatása a konténeren belül:

`ddev exec {{echo 1}}`
