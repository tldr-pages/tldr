# run-mailcap

> MailCap programok futtatása.
> A mailcap megtekintése, megtekintése, szerkesztése, összeállítása, nyomtatása - a mailcap fájlban (vagy annak bármelyik aliasában)
> található bejegyzéseken keresztül végrehajtott programok a megadott műveletet használják az egyes mime-típusok/fájlok feldolgozására.
> További információ: <https://manned.org/run-mailcap>.

- A run-mailcap egyes műveletei/programjai action flaggel hívhatók meg:

`run-mailcap --action=ACTION [--option[=value]]`

- Egyszerűbben fogalmazva:

`run-mailcap --action=ACTION {{filename}}`

- Kapcsolja be az extra információkat:

`run-mailcap --action=ACTION --debug {{filename}}`

- A "copiousoutput" utasítás figyelmen kívül hagyása és a kimenet továbbítása a standard kimenetre:

`run-mailcap --action=ACTION --nopager {{filename}}`

- A megtalált parancs megjelenítése anélkül, hogy ténylegesen végrehajtaná azt:

`run-mailcap --action=ACTION --norun {{filename}}`
