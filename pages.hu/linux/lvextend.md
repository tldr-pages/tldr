# lvextend

> A logikai kötet méretének növelése. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvextend.8.html>.

- Egy kötet méretének növelése 120 GB-ra:

`lvextend --size {{120G}} {{logical_volume}}`

- Egy kötet méretének 40 GB-tal való növelése, valamint a mögöttes fájlrendszer növelése:

`lvextend --size +{{40G}} -r {{logical_volume}}`

- Egy kötet méretének növelése a szabad fizikai kötetterület 100%-ára:

`lvextend --size {{100}}%FREE {{logical_volume}}`
