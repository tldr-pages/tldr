# dolt merge

> Két vagy több fejlesztési történet összekapcsolása. További információ: <https://github.com/dolthub/dolt>.

- A megnevezett commitok változásainak beemelése az aktuális ágba:

`dolt merge {{branch_name}}`

- A megnevezett commitok változásainak beemelése az aktuális ágba a commit-előzmények frissítése nélkül:

`dolt merge --squash {{branch_name}}`

- Összevon egy ágat, és létrehoz egy egyesítési commitot akkor is, ha az egyesítés gyorsított előzményként oldódik fel:

`dolt merge --no-ff {{branch_name}}`

- Egy ág egyesítése és egyesítési commit létrehozása egy adott commit üzenettel:

`dolt merge --no-ff -m "{{message}}" {{branch_name}}`

- Az aktuális konfliktusfeloldási folyamat megszakítása:

`dolt merge --abort`
