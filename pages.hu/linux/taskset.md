# taskset

> Egy folyamat CPU-affinitásának lekérdezése vagy beállítása, illetve új folyamat indítása meghatározott CPU-affinitással. További információ: <https://manned.org/taskset>.

- Egy futó folyamat CPU-affinitásának lekérdezése PID alapján:

`taskset --pid --cpu-list {{pid}}`

- Egy futó folyamat CPU-affinitásának beállítása PID alapján:

`taskset --pid --cpu-list {{cpu_id}} {{pid}}`

- Új folyamat indítása egyetlen CPU-hoz való affinitással:

`taskset --cpu-list {{cpu_id}} {{command}}`

- Új folyamat indítása több, nem egymást követő CPU-hoz való affinitással:

`taskset --cpu-list {{cpu_id_1}},{{cpu_id_2}},{{cpu_id_3}}`

- Új folyamat indítása az 1-4. CPU-hoz való affinitással:

`taskset --cpu-list {{cpu_id_1}}-{{cpu_id_4}}`
