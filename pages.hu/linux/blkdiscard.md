# blkdiscard

> A tárolóeszközökön lévő eszközszektorok selejtezése. Hasznos SSD-k esetében. További információ: <https://manned.org/blkdiscard>.

- Az eszköz összes szektorának eldobása, az összes adat eltávolításával:

`blkdiscard /dev/{{device}}`

- Biztonságosan eldobja az összes blokkot egy eszközön, eltávolítva az összes adatot:

`blkdiscard --secure /dev/{{device}}`

- Az eszköz első 100 MB-jának eldobása:

`blkdiscard --length {{100MB}} /dev/{{device}}`
