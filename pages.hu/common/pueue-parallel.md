# pueue parallel

> Az engedélyezett párhuzamos feladatok mennyiségének beállítása. További információ: <https://github.com/Nukesor/pueue>.

- Állítsa be a párhuzamosan futtatható feladatok maximális számát az alapértelmezett csoportban:

`pueue parallel {{max_number_of_parallel_tasks}}`

- Állítsa be a párhuzamosan futtatható feladatok maximális számát egy adott csoportban:

`pueue parallel --group {{group_name}} {{maximum_number_of_parallel_tasks}}`
