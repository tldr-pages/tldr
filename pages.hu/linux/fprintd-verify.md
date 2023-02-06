# fprintd-verify

> Ujjlenyomatok ellenőrzése az adatbázis alapján. További információ: <https://manned.org/fprintd-verify>.

- Az aktuális felhasználó összes tárolt ujjlenyomatának ellenőrzése:

`fprintd-verify`

- Egy adott ujjlenyomat ellenőrzése az aktuális felhasználóhoz:

`fprintd-verify --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- Egy adott felhasználó ujjlenyomatainak ellenőrzése:

`fprint-verify {{username}}`

- Egy adott felhasználó egy adott ujjlenyomatának ellenőrzése:

`fprintd-verify --finger {{finger_name}} {{username}}`

- A folyamat meghiúsul, ha az ujjlenyomat nem egyezik az adatbázisban az aktuális felhasználóhoz tárolt ujjlenyomatokkal:

`fprint-verify --g-fatal-warnings`

- Súgó megjelenítése:

`fprintd-verify --help`
