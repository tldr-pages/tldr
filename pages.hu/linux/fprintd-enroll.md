# fprintd-enroll

> Ujjlenyomatok felvétele az adatbázisba. További információ: <https://manned.org/fprintd-enroll>.

- Az aktuális felhasználó jobb mutatóujjának bejegyzése:

`fprintd-enroll`

- Egy adott ujj bejegyzése az aktuális felhasználóhoz:

`fprintd-enroll --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- Regisztrálja a jobb mutatóujjat egy adott felhasználóhoz:

`fprintd-enroll {{username}}`

- Egy adott ujj beiratkozása egy adott felhasználóhoz:

`fprintd-enroll --finger {{finger_name}} {{username}}`

- Súgó megjelenítése:

`fprintd-enroll --help`
