# pueue edit

> Egy elrejtett vagy sorba állított feladat parancsának vagy elérési útvonalának szerkesztése. További információ: <https://github.com/Nukesor/pueue>.

- Feladat szerkesztése, a feladat azonosítójának lekérdezéséhez lásd: `pueue status`:

`pueue edit {{task_id}}`

- Szerkessze az elérési utat, ahonnan egy feladat végrehajtásra kerül:

`pueue edit {{task_id}} --path`

- Parancs szerkesztése a megadott szerkesztővel:

`EDITOR={{nano}} pueue edit {{task_id}}`
