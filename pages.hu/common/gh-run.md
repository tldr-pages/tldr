# gh run

> A legutóbbi GitHub Actions munkafolyamatok megtekintése, futtatása és megtekintése. További információ: <https://cli.github.com/manual/gh_run>.

- Interaktívan válasszon ki egy futtatást a munkákról szóló információk megtekintéséhez:

`gh run view`

- Egy adott futtatással kapcsolatos információk megjelenítése:

`gh run view {{workflow_run_number}}`

- Információk megjelenítése egy munka lépéseiről:

`gh run view --job={{job_number}}`

- Egy munka naplójának megjelenítése:

`gh run view --job={{job_number}} --log`

- Egy adott munkafolyamat ellenőrzése és kilépés nem nulla státusszal, ha a futtatás sikertelen volt:

`gh run view {{workflow_run_number}} --exit-status && {{echo "run pending or passed"}}`

- Interaktívan kiválaszthat egy aktív futtatást, és megvárhatja, amíg befejeződik:

`gh run watch`

- Egy futtatáshoz tartozó munkák megjelenítése és várakozás, amíg az elkészül:

`gh run watch {{workflow_run_number}}`

- Egy adott munkafolyamat újrafuttatása:

`gh run rerun {{workflow_run_number}}`
