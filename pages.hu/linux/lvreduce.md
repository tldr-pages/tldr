# lvreduce

> Egy logikai kötet méretének csökkentése. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvreduce.8.html>.

- Egy kötet méretének csökkentése 120 GB-ra:

`lvreduce --size {{120G}} {{logical_volume}}`

- Egy kötet méretének csökkentése 40 GB-tal, valamint az alapul szolgáló fájlrendszer méretének csökkentése:

`lvreduce --size -{{40G}} -r {{logical_volume}}`
