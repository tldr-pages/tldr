# cradle sql

> A Cradle SQL-adatbázisok kezelése. További információ: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Állítsa újra az adatbázis sémáját:

`cradle sql build`

- Újraépíti az adatbázis sémáját egy adott csomaghoz:

`cradle sql build {{package_name}}`

- A teljes adatbázis kiürítése:

`cradle sql flush`

- Az adatbázis tábláinak kiürítése egy adott csomaghoz:

`cradle sql flush {{package_name}}`

- Az összes csomag tábláinak feltöltése:

`cradle sql populate`

- Egy adott csomag táblázatainak feltöltése:

`cradle sql populate {{package_name}}`
