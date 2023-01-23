# foreman

> Procfile-alapú alkalmazások kezelése. További információ: <https://manned.org/foreman>.

- Indítson el egy alkalmazást az aktuális könyvtárban lévő Procfile-lal:

`foreman start`

- Alkalmazás indítása egy megadott Procfile-lal:

`foreman start -f {{Procfile}}`

- Egy adott alkalmazás indítása:

`foreman start {{process}}`

- Procfile formátumának hitelesítése:

`foreman check`

- Egyszeri parancsok futtatása a folyamat környezetével:

`foreman run {{command}}`

- Az összes folyamat indítása a "worker" nevű kivételével:

`foreman start -m all=1,{{worker}}=0`
