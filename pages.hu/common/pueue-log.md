# pueue log

> 1 vagy több feladat naplókimenetének megjelenítése. Lásd még: `pueue status`. További információ: <https://github.com/Nukesor/pueue>.

- Megjeleníti az összes feladat utolsó néhány kimeneti sorát:

`pueue log`

- Egy feladat teljes kimenetének megjelenítése:

`pueue log {{task_id}}`

- Több feladat kimenetének utolsó néhány sorának megjelenítése:

`pueue log {{task_id}} {{task_id}}`

- Adott számú sor kiírása a kimenet végéből:

`pueue log --lines {{number_of_lines}} {{task_id}}`
