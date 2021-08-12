# taskset

> Obțineți sau setați afinitatea procesorului unui proces sau începeți un proces nou cu o afinitate definită a procesorului.

- Obțineți un proces de funcționare „afinitate CPU prin PID:

`taskset --pid --cpu-list {{pid}}`

- Setați un proces de rulare' afinitate CPU prin PID:

`taskset --pid --cpu-list {{cpu_id}} {{pid}}`

- Începeți un nou proces cu afinitate pentru un singur procesor:

`taskset --cpu-list {{cpu_id}} {{command}}`

- Începeți un nou proces cu afinitate pentru mai multe procesoare non-secvențiale:

`taskset --cpu-list {{cpu_id_1}} {{cpu_id_2}} {{cpu_id_3}}`

- Începeți un nou proces cu afinitate pentru procesoarele de la 1 la 4:

`taskset --cpu-list {{cpu_id_1}},{{cpu_id_4}}`
