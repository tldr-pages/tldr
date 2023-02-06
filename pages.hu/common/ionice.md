# ionice

> A program I/O ütemezési osztályának és prioritásának lekérése vagy beállítása. Ütemezési osztályok: Prioritási szintek: 0 (a legmagasabb) - 7 (a legalacsonyabb). További információ: https: [//manned.org/ionice](https://manned.org/ionice).

- Egy futó folyamat I/O ütemezési osztályának beállítása:

`ionice -c {{scheduling_class}} -p {{pid}}`

- Futtasson egy parancsot egyéni I/O ütemezési osztállyal és prioritással:

`ionice -c {{scheduling_class}} -n {{priority}} {{command}}`

- Nyomtassa ki a futó folyamat I/O ütemezési osztályát és prioritását:

`ionice -p {{pid}}`
