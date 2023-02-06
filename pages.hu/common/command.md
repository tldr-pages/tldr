# command

> A parancs arra kényszeríti a héjat, hogy a programot futtassa, és figyelmen kívül hagyja az azonos nevű függvényeket, beépített programokat és aliasokat. További információ: <https://manned.org/command>.

- A `ls` program szó szerinti végrehajtása, még akkor is, ha létezik egy `ls` alias:

`command {{ls}}`

- A futtatható program elérési útvonalának vagy egy adott parancs alias-definíciójának megjelenítése:

`command -v {{command_name}}`
