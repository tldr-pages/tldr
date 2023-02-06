# lvresize

> A logikai kötet méretének módosítása. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvresize.8.html>.

- A logikai kötet méretének módosítása 120 GB-ra:

`lvresize --size {{120G}} {{volume_group}}/{{logical_volume}}`

- Egy logikai kötet, valamint az alapul szolgáló fájlrendszer méretének 120 GB-tal történő bővítése:

`lvresize --size +{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`

- A logikai kötet méretének kiterjesztése a szabad fizikai kötetterület 100%-ára:

`lvresize --size {{100}}%FREE {{volume_group}}/{{logical_volume}}`

- A logikai kötet és a mögöttes fájlrendszer méretének csökkentése 120 GB-tal:

`lvresize --size -{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`
