# bg

> Folytatja a felfüggesztett (pl. a `Ctrl + Z`) munkákat, és a háttérben tartja őket. További információ: <https://manned.org/bg>.

- A legutóbb felfüggesztett feladat újraindítása és a háttérben történő futtatása:

`bg`

- Egy adott feladat újraindítása (a `jobs -l` segítségével megkapja az azonosítóját) és futtatása a háttérben:

`bg %{{job_id}}`
