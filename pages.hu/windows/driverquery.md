# driverquery

> A telepített eszközillesztőkkel kapcsolatos információk megjelenítése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- Az összes telepített eszközillesztőprogram listájának megjelenítése:

`driverquery`

- Az illesztőprogramok listájának megjelenítése a megadott formátumban:

`driverquery /fo {{table|list|csv}}`

- Megjeleníti az illesztőprogramok listáját egy oszlopban, amely jelzi, hogy aláírtak-e:

`driverquery /si`

- A fejléc kizárása a kimeneti listából:

`driverquery /nh`

- Távoli gép illesztőprogramjainak listájának megjelenítése:

`driverquery /s {{hostname}} /u {{username}} /p {{password}}`

- Az illesztőprogramok listájának megjelenítése részletes információkkal:

`driverquery /v`

- Részletes használati információk megjelenítése:

`driverquery /?`
