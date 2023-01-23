# tlmgr conf

> A TeX Live konfiguráció kezelése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az aktuális TeX Live konfiguráció megjelenítése:

`tlmgr conf`

- Az aktuális `texmf`, `tlmgr` vagy `updmap` konfiguráció megjelenítése:

`tlmgr conf {{texmf|tlmgr|updmap}}`

- Csak egy adott konfigurációs opció megjelenítése:

`tlmgr conf {{texmf|tlmgr|updmap}} {{configuration_key}}`

- Egy adott konfigurációs opció beállítása:

`tlmgr conf {{texmf|tlmgr|updmap}} {{configuration_key}} {{value}}`

- Egy adott konfigurációs opció törlése:

`tlmgr conf {{texmf|tlmgr|updmap}} --delete {{configuration_key}}`

- A rendszerhívások végrehajtásának letiltása a `\write18` oldalon keresztül:

`tlmgr conf texmf {{shell_escape}} {{0}}`

- Minden további `texmf` fa megjelenítése:

`tlmgr conf auxtrees show`
