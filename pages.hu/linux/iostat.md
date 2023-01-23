# iostat

> Eszközök és partíciók statisztikáinak jelentése. További információ: <https://manned.org/iostat>.

- A rendszer indítása óta a CPU- és lemezstatisztikákról szóló jelentés megjelenítése:

`iostat`

- A CPU- és lemezstatisztikák jelentésének megjelenítése megabájtra átszámított egységekkel:

`iostat -m`

- CPU-statisztikák megjelenítése:

`iostat -c`

- Lemezstatisztikák megjelenítése lemeznevekkel (beleértve az LVM-et is):

`iostat -N`

- Bővített lemezstatisztikák megjelenítése lemeznevekkel az "sda" eszközhöz:

`iostat -xN {{sda}}`

- A CPU- és lemezstatisztikák 2 másodpercenkénti növekményes jelentéseinek megjelenítése:

`iostat {{2}}`
