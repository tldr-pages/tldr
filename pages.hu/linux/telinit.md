# telinit

> SysV runlevel módosítása. Mivel a SysV runlevelek koncepciója elavult, a runlevel kérések átláthatóan systemd egységaktiválási kérésekké lesznek fordítva. További információ: <https://manned.org/telinit>.

- Kapcsolja ki a gépet:

`telinit 0`

- A gép újraindítása:

`telinit 6`

- SysV futási szint módosítása:

`telinit {{2|3|4|5}}`

- Váltás mentési üzemmódra:

`telinit 1`

- A démon konfigurációjának újratöltése:

`telinit q`

- Ne küldjön falüzenetet újraindítás/kikapcsolás előtt (6/0):

`telinit --no-wall {{value}}`
